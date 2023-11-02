import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode

from dotenv import load_dotenv

load_dotenv()

dispatcher = Dispatcher()

@dispatcher.message()
async def process_message(context: Message):
    print('message ->', context.chat.id, context.chat.username, '/', context.text)

    await context.answer("Hello world!")

async def main():
    bot = Bot(os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)

    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
