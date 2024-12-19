import logging

from aiogram import F, Router
from aiogram.types import (
    Message,
    FSInputFile
)

from thingspeak_api import get_latest_value, get_n_latest_values
from create_img import create_and_save_img, get_full_file_name
from utils import remove_file


router = Router()


@router.message(F.text.startswith("/c"))
async def get_c02_handler(message: Message) -> None:
    """
    Get latest CO2 value
    """

    logging.info("Getting latest value for CO2 (field4)")
    latest_co2_value, time = await get_latest_value(field_id=4)
    await message.answer(f"Latest CO2 -> <b>{latest_co2_value}</b> <pre>  at {time}</pre>")


@router.message(F.text.startswith("/f"))
async def get_file_handler(message: Message) -> None:
    """
    Get file
    """

    logging.info("Getting latest values as an image")
    latest_values, interval = await get_n_latest_values(field_id=4)
    create_and_save_img(latest_values, interval)
    file_name = f"{interval}.png"
    file = FSInputFile(file_name)
    await message.answer_document(document=file)
    remove_file(get_full_file_name(file_name))