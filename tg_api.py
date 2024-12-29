import logging
from numbers import Number

import requests
from requests.exceptions import Timeout

logger = logging.getLogger("telegram.api")

TG_SEND_MESSAGE_URL = (
    "https://api.telegram.org/{bot}/sendMessage?"
    "&chat_id={chat_id}&text={msg}"
)


class TelegramAPIError(Exception):
    def __init__(self, message):
        self.message = "TelegramAPIError: " + message


async def make_tg_request(url):
    logger.info("Making TelegramAPI request")
    logger.info(url)
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code >= 300:
            raise TelegramAPIError(f"status {resp.status_code}")
    except Timeout as e:
        raise TelegramAPIError("TelegramAPI timeout error") from e
    # resp = response.json()
    # raise Exception(f"TelegramAPI error: {resp.get('status')} - {resp.get('error')}")  # noqa: E501


async def send_message(bot: str, chat_id: Number, msg: str):
    url = TG_SEND_MESSAGE_URL.format(
        bot=bot,
        chat_id=chat_id,
        msg=msg,
    )
    await make_tg_request(url)
