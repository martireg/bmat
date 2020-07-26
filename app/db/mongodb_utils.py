from motor.motor_asyncio import AsyncIOMotorClient
from app.config import (
    MONGO_HOST,
    MONGO_PORT,
    MAX_CONNECTIONS_COUNT,
    MIN_CONNECTIONS_COUNT,
)
from app.db.mongodb import db


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(
        MONGO_HOST,
        MONGO_PORT,
        maxPoolSize=MAX_CONNECTIONS_COUNT,
        minPoolSize=MIN_CONNECTIONS_COUNT,
    )


async def close_mongo_connection():
    db.client.close()
