import logging
import requests
from datetime import datetime
from numbers import Number

logger = logging.getLogger("ts_api")

TIMEZONE_HOURS_OFFSET = 2
TS_CHANNEL_ID = 386789
TS_READ_FIELD_URL = (
    "https://api.thingspeak.com/channels/{channel_id}/fields/{field_id}.json?results={results_number}"
)


async def make_thingspeak_request(url):
    logger.info("Making ThingSpeak request")
    logger.info(url)
    response = requests.get(url)
    if response.status_code < 300:
        json_response = response.json()
        if not json_response:
            raise Exception(f"ThingSpeakAPI response couldn't be parsed")
        return json_response
    else:
        json_response = response.json()
        raise Exception(f"ThingSpeakAPI error: {json_response.get('status')} - {json_response.get('error')}")


async def get_latest_value(field_id: Number = 1):
    url = TS_READ_FIELD_URL.format(
        channel_id=TS_CHANNEL_ID,
        field_id=field_id,
        results_number=1
    )
    json_response = await make_thingspeak_request(url)
    try:
        field_feeds = json_response.get("feeds", [])
        value = field_feeds[0].get(f"field{field_id}")
        timestamp = field_feeds[0].get("created_at")
        time = datetime.fromisoformat(timestamp)
        time = time.replace(hour=time.hour + TIMEZONE_HOURS_OFFSET)
        time = time.time().isoformat()
        return value, time
    except Exception as e:
        raise Exception(f"ThingSpeakAPI parse error: {str(e)}")


async def get_n_latest_values(field_id: Number = 1, results_number: Number = 100):
    url = TS_READ_FIELD_URL.format(
        channel_id=TS_CHANNEL_ID,
        field_id=field_id,
        results_number=results_number
    )
    json_response = await make_thingspeak_request(url)
    try:
        field_feeds = json_response.get("feeds", [])
        latest_values = map(lambda o: int(o[f"field{field_id}"]), field_feeds)
        return list(latest_values)
    except Exception as e:
        raise Exception(f"ThingSpeakAPI parse error: {str(e)}")
