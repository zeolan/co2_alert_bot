from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from tgbot_commands import router
from app_logging import logger
from env_vars import BOT_TOKEN


async def bot_polling_task():
    # Initialize Bot instance with default bot properties
    # which will be passed to all API calls
    bot = Bot(token=BOT_TOKEN,
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
