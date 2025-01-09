import asyncio

from app_logging import logger
from thingspeak_api import get_latest_value
from tg_api import send_message
from env_vars import BOT_TOKEN


CO2_CHECK_INTERVAL = 2 * 60
CO2_MAX_LEVEL = 1300
TG_CHAT_ID = 1175693746

co2_level_alarm = False


async def co2_check_task():
    global co2_level_alarm
    while True:
        logger.info("CO2 Level Check")
        latest_co2_value, _time = await get_latest_value(field_id=4)
        latest_co2_value = int(latest_co2_value)
        if latest_co2_value >= CO2_MAX_LEVEL and not co2_level_alarm:
            co2_level_alarm = True
            await send_message(bot=BOT_TOKEN,
                               chat_id=TG_CHAT_ID,
                               msg=f"ALARM -> {latest_co2_value}")
        elif latest_co2_value < CO2_MAX_LEVEL and co2_level_alarm:
            co2_level_alarm = False
            await send_message(bot=BOT_TOKEN,
                               chat_id=TG_CHAT_ID,
                               msg=f"OK -> {latest_co2_value}")
        await asyncio.sleep(CO2_CHECK_INTERVAL)
