import asyncio
import logging
import sys
import re
from os import getenv
# from typing import Any, Dict

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    FSInputFile
)

from dotenv import load_dotenv

from thingspeak_api import get_latest_value, get_n_latest_values
from create_img import create_and_save_img

load_dotenv()


TOKEN = getenv("BOT_TOKEN")

router = Router()


@router.message(F.text.startswith("/#"))
async def get_c02_handler(message: Message) -> None:
    """
    Get latest CO2 value
    """

    logging.info("Getting latest value for CO2 (field4)")
    latest_co2_value = await get_latest_value(field_id=4)
    await message.answer(f"Latest CO2 -> {latest_co2_value}")


@router.message(F.text.startswith("/f"))
async def get_file_handler(message: Message) -> None:
    """
    Get file
    """

    logging.info("Getting latest values as an image")
    latest_values = await get_n_latest_values(field_id=4, results_number=200)
    create_and_save_img(latest_values)
    file = FSInputFile("image.png")
    await message.answer_document(document=file)


async def main():
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.include_router(router)

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

