from typing import List, Dict

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from pydantic import create_model
from starlette.responses import StreamingResponse, Response

from app.business_layers.domain import Work
from app.business_layers.repository import WorkRepository
from app.business_layers.use_cases import (
    bulk_upload_works_use_case,
    get_work_use_case,
    list_works_use_case,
)
from app.db.mongodb import get_client
from app.utils.csv_manipulation import process_csv, create_csv


async def get_db():
    return await get_client()


work_router = APIRouter()

# Model Fields are defined by either a tuple of the form (<type>, <default value>) or a default value
annotations = {k: (v, ...) for k, v in Work.__annotations__.items()}
WorkModel = create_model("WorkModel", **annotations)


@work_router.post("/upload_file", response_model=List[WorkModel])
async def upload_csv(file: UploadFile = File(...), db=Depends(get_db)) -> List[Dict]:
    csv = process_csv(await file.read())
    works = await bulk_upload_works_use_case(WorkRepository(db), csv)
    return [work.to_dict() for work in works]


@work_router.get("/download_file")
async def download_csv(db=Depends(get_db)) -> File:
    works = await list_works(db)
    response = Response(create_csv(works), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response


@work_router.get("/work/{iswc}", response_model=WorkModel)
async def get_work(iswc: str, db=Depends(get_db)):
    work = await get_work_use_case(WorkRepository(db), iswc)
    if not work:
        raise HTTPException(status_code=404, detail="Item not found")
    return work.to_dict()


@work_router.get("/works", response_model=List[WorkModel])
async def list_works(db=Depends(get_db)):
    return [work.to_dict() for work in await list_works_use_case(WorkRepository(db))]
