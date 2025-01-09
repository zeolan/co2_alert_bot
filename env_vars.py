from os import getenv

from dotenv import load_dotenv

load_dotenv()


def get_env_var(name: str):
    if not getenv(name):
        raise ValueError(f"Environment variable {name} not set")
    return getenv(name)


BOT_TOKEN = get_env_var("BOT_TOKEN")
