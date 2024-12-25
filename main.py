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

co2_level_alarm = False


async def main():
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.include_router(router)

    # Start event dispatching
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Exception in polling: {str(e)}")
        await dp.stop_polling()

# async def poll_co2():
#     co2_level_alarm = False
#     try:
#         logger.info("Getting latest value for CO2 (field4)")
#         latest_co2_value, time = await get_latest_value(field_id=4)
#         if int(latest_co2_value) >= 1300 and not co2_level_alarm:
#             await tg_bot_send_message(f"ALARM -> {latest_co2_value}")
#             co2_level_alarm = True
#         elif int(latest_co2_value) < 1300 and co2_level_alarm:
#             await tg_bot_send_message(f"OK -> {latest_co2_value}")
#             co2_level_alarm = False
#         #send_tg_bot_message(latestCO2_value)
#     except Exception as e:
#         await tg_bot_send_message(f"Exception -> {str(e)}")


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Exception in main: {str(e)}")
