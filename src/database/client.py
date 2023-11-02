import os

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

client = AsyncIOMotorClient(os.getenv("DB_URL"), server_api=ServerApi("1"))
database = client[os.getenv("DB_NAME")]

DB_COLLECTION = os.getenv("DB_COLLECTION")
