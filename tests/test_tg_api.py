import pytest
import unittest.mock as mock

from requests.exceptions import Timeout

from tg_api import (
    make_tg_request,
    send_message,
    TelegramAPIError
)


@pytest.mark.asyncio
@mock.patch("tg_api.requests.get")
async def test_make_tg_request_1(mock_obj):
    mock_obj.return_value.status_code = 500
    with pytest.raises(TelegramAPIError):
        await make_tg_request("FAKE_URL")


@pytest.mark.asyncio
@mock.patch("tg_api.requests.get")
async def test_make_tg_request_2(mock_obj):
    mock_obj.return_value.status_code = 200
    response = await make_tg_request("FAKE_URL")
    assert response is None


@pytest.mark.asyncio
@mock.patch("tg_api.requests.get", side_effect=Timeout)
async def test_make_tg_request_3(mock_obj):
    mock_obj.return_value.status_code = 200
    with pytest.raises(TelegramAPIError):
        await make_tg_request("FAKE_URL")


@pytest.mark.asyncio
@mock.patch("tg_api.make_tg_request")
async def test_send_message(mock_obj):
    mock_obj.return_value.status_code = 200
    response = await send_message(bot="BOT_TOKEN",
                                  chat_id=123456789,
                                  msg="Test")
    assert response is None
