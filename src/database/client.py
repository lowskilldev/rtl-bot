from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.config import config

client = AsyncIOMotorClient(config.DB_URL, server_api=ServerApi("1"))
database = client[config.DB_NAME]

DB_COLLECTION = config.DB_COLLECTION