import asyncio
import logging
import sys
import json

from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode

from src.config import config
from src.database.funcs import aggregate_payouts

dispatcher = Dispatcher()

@dispatcher.message()
async def process_message(context: Message):
    try:
        query = json.loads(context.text)

        if "dt_from" not in query or "dt_upto" not in query or "group_type" not in query:
            await context.answer("wrong input")

            return

        if query["group_type"] not in ["month", "hour", "day"]:
            await context.answer("wrong [group_type] parameter")

            return

        start_date = datetime.fromisoformat(query["dt_from"])
        end_date = datetime.fromisoformat(query["dt_upto"])

        response = await aggregate_payouts(start_date, end_date, query["group_type"])

        await context.answer(json.dumps(response))
    except Exception as e:
        await context.answer(str(e))

async def main():
    bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)

    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

