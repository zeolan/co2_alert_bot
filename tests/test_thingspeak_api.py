import datetime
import pytest
import unittest.mock as mock

from thingspeak_api import (
    get_latest_value,
    get_n_latest_values,
    make_thingspeak_request,
    ThingSpeakAPIError
)

FAKE_DATA = {
        "feeds": [
            {
                "field1": "500",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "field1": "500",
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
    }
FAKE_WRONG_DATA = {
        "feeds": [
            {
                "field1": "500",
                "created_at": False
            },
            {
                "field1": "500",
                "created_at": False
            }
        ]
    }


def json_fn(json_data):
    def inner_json():
        return json_data
    return inner_json


@pytest.mark.asyncio
@mock.patch("thingspeak_api.requests.get")
async def test_make_thingspeak_request_1(mock_obj):
    mock_obj.return_value.status_code = 500
    with pytest.raises(ThingSpeakAPIError):
        await make_thingspeak_request("FAKE_URL")


@pytest.mark.asyncio
@mock.patch("thingspeak_api.requests.get")
async def test_make_thingspeak_request_2(mock_obj):
    mock_obj.return_value.json = json_fn(FAKE_DATA)
    mock_obj.return_value.status_code = 200
    response = await make_thingspeak_request("FAKE_URL")
    assert response == FAKE_DATA


@pytest.mark.asyncio
@mock.patch("thingspeak_api.requests.get")
async def test_make_thingspeak_request_3(mock_obj):
    mock_obj.return_value.json = json_fn(None)
    mock_obj.return_value.status_code = 200
    with pytest.raises(ThingSpeakAPIError):
        await make_thingspeak_request("FAKE_URL")


@pytest.mark.asyncio
@mock.patch("thingspeak_api.make_thingspeak_request")
async def test_get_latest_value_1(mock_obj):
    mock_obj.return_value = FAKE_WRONG_DATA
    with pytest.raises(ThingSpeakAPIError):
        await get_latest_value(1)


@pytest.mark.asyncio
@mock.patch("thingspeak_api.make_thingspeak_request")
async def test_get_latest_value_2(mock_obj):
    mock_obj.return_value = FAKE_DATA
    value, _ = await get_latest_value(1)
    assert value == FAKE_DATA["feeds"][0]["field1"]


@pytest.mark.asyncio
@mock.patch("thingspeak_api.make_thingspeak_request")
async def test_get_n_latest_values_1(mock_obj):
    mock_obj.return_value = FAKE_WRONG_DATA
    with pytest.raises(ThingSpeakAPIError):
        await get_n_latest_values(1)


@pytest.mark.asyncio
@mock.patch("thingspeak_api.make_thingspeak_request")
async def test_get_n_latest_values_2(mock_obj):
    mock_obj.return_value = FAKE_DATA
    values, _ = await get_n_latest_values(1)
    print(values)
    assert values == [int(value["field1"]) for value in FAKE_DATA["feeds"]]
