import asyncio
# import logging
# import sys
# import time
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
CHECK_INTERVAL = 60
HEALTH_CHECK_INTERVAL = 20 * 60

co2_level_alarm = False


async def main():
    # Initialize Bot instance with default bot properties
    # which will be passed to all API calls
    bot = Bot(token=TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML)
              )

    dp = Dispatcher()

    dp.include_router(router)

    # Start event dispatching
    while True:
        try:
            await dp.start_polling(bot)
        except Exception as e:
            logger.error(f"Exception in polling: {str(e)}")
            await dp.stop_polling()


async def health_check():
    while True:
        logger.info("Health Check")
        await asyncio.sleep(HEALTH_CHECK_INTERVAL)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        health_check_task = loop.create_task(health_check())
        bot_task = loop.create_task(main())
        loop.run_until_complete(health_check_task)
        loop.run_until_complete(bot_task)
    except (asyncio.CancelledError, KeyboardInterrupt):
        health_check_task.cancel()
        bot_task.cancel()
    except Exception as e:
        logger.error(f"Exception in main: {str(e)}")
