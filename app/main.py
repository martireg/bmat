from fastapi import FastAPI

from app.business_layers.presentation import work_router
from app.db.mongodb_utils import connect_to_mongo


app = FastAPI(docs_url="/")
app.include_router(work_router, tags=["works"])


app.on_event("startup")(connect_to_mongo)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=5000)
