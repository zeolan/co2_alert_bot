from datetime import datetime, timedelta
import os
import logging

loger = logging.getLogger()

TIMEZONE_HOURS_OFFSET = 2


def get_local_datetime(dt):
    return datetime.fromisoformat(dt) + timedelta(hours=TIMEZONE_HOURS_OFFSET)

def remove_file(file_name: str) -> None:
    try:
        os.remove(file_name)
    except FileNotFoundError:
        loger.warning(f"Trying to remove not existing file: {file_name}")