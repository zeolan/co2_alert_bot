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
from thingspeak_api import get_latest_value
from tg_api import send_message


load_dotenv()

TOKEN = getenv("BOT_TOKEN")
HEALTH_CHECK_INTERVAL = 20 * 60
CO2_CHECK_INTERVAL = 2 * 60
CO2_MAX_LEVEL = 1300
TG_CHAT_ID = 1175693746


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
            logger.error("Exception in polling: %s", str(e))
            await dp.stop_polling()


# async def health_check():
#     while True:
#         logger.info("Health Check")
#         await asyncio.sleep(HEALTH_CHECK_INTERVAL)


async def co2_level_check():
    co2_level_alarm = False
    while True:
        logger.info("CO2 Level Check")
        latest_co2_value, _time = await get_latest_value(field_id=4)
        latest_co2_value = int(latest_co2_value)
        if latest_co2_value >= CO2_MAX_LEVEL and not co2_level_alarm:
            co2_level_alarm = True
            send_message(bot=TOKEN,
                         chat_id=TG_CHAT_ID,
                         msg=("ALARM -> %s", latest_co2_value))
        elif latest_co2_value < CO2_MAX_LEVEL and co2_level_alarm:
            co2_level_alarm = False
            send_message(bot=TOKEN,
                         chat_id=TG_CHAT_ID,
                         msg=("OK -> %s", latest_co2_value))
        await asyncio.sleep(CO2_CHECK_INTERVAL)


if __name__ == "__main__":
    logger.info("================== START ==================")
    try:
        loop = asyncio.get_event_loop()
        # health_check_task = loop.create_task(health_check())
        co2_level_check_task = loop.create_task(co2_level_check())
        bot_task = loop.create_task(main())
        # loop.run_until_complete(health_check_task)
        loop.run_until_complete(co2_level_check_task)
        loop.run_until_complete(bot_task)
    except (asyncio.CancelledError, KeyboardInterrupt):
        # health_check_task.cancel()
        bot_task.cancel()
        co2_level_check_task.cancel()
    except Exception as e:
        logger.error("Exception in main: %s", str(e))
