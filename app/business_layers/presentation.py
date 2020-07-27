from fastapi import APIRouter, UploadFile, File

from app.db.mongodb import get_client
from app.utils.csv_manipulation import process_csv
from app.business_layers.repository import WorkRepository
from app.business_layers.use_cases import bulk_upload_works_use_case

work_router = APIRouter()


@work_router.post("/upload_file")
async def upload_csv(file: UploadFile = File(...)):
    read = await file.read()
    csv = process_csv(read)
    client = await get_client()
    works = await bulk_upload_works_use_case(WorkRepository(client), csv)
    return [work.to_dict() for work in works]
