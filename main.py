import asyncio
import logging
import sys
from os import getenv
# from typing import Any, Dict

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv

from tgbot_commands import router
from app_logging import logger


load_dotenv()


TOKEN = getenv("BOT_TOKEN")


async def main():
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.include_router(router)

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except Exception as e:
        logger.info(f"Exception in main: {str(e)}")

