import logging
from typing import Optional, Union, List

from motor.motor_asyncio import AsyncIOMotorClient

from app.business_layers.domain import Work


class WorkRepository:
    def __init__(self, db_client: AsyncIOMotorClient):
        self.db_client = db_client

    async def create(self, work: dict) -> Work:
        insert = await self.db_client.bmat.works.insert_one(work)
        logging.debug("inserted work id: %", insert.inserted_id)
        return Work.from_dict(work)

    async def create_many(self, works: List[dict]) -> List[Work]:
        await self.db_client.bmat.works.insert_many(works)
        return [Work.from_dict(work) for work in works]

    async def get_works(self, filters: Optional[dict] = None) -> List[Work]:
        if filters is None:
            filters = {}
        cursor = self.db_client.bmat.works.find(filters)
        works = await cursor.to_list(None)
        return [Work.from_dict(work) for work in works]

    async def first(self, query: dict) -> Union[Work, None]:
        work = await self.db_client.bmat.works.find_one(query)
        return Work.from_dict(work) if work is not None else None

    async def update(self, query: dict, parameters: dict) -> None:
        await self.db_client.bmat.works.update(query, parameters)
