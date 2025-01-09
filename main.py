import asyncio

from app_logging import logger
from tasks.co2_check_task import co2_check_task
from tasks.bot_polling_task import bot_polling_task


if __name__ == "__main__":
    logger.info("================== START ==================")
    try:
        loop = asyncio.get_event_loop()
        co2_task = loop.create_task(co2_check_task())
        bot_task = loop.create_task(bot_polling_task())
        loop.run_until_complete(co2_task)
        loop.run_until_complete(bot_task)
    except (asyncio.CancelledError, KeyboardInterrupt):
        bot_task.cancel()
        co2_task.cancel()
    except Exception as e:  # pylint: disable=W0718
        logger.error("Exception in main: %s", str(e))
