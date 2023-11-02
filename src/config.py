import os

from typing import Any

from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN: str
    DB_URL: str
    DB_NAME: str   
    DB_COLLECTION: str 

    def __getattribute__(self, __name: str) -> Any:
        return os.getenv(__name)

config = Config()
