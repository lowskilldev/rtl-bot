import os

from dotenv import load_dotenv

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from datetime import datetime

load_dotenv()

client = AsyncIOMotorClient(os.getenv("DB_URL"), server_api=ServerApi("1"))
database = client[os.getenv("DB_NAME")]

async def aggregate_payouts(start_date: datetime, end_date: datetime, group_type="month"):
    pass
