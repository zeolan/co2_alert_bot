import datetime
import pytest

from utils import remove_file, get_local_datetime, TIMEZONE_HOURS_OFFSET


def test_remove_file():
    with pytest.raises(FileNotFoundError):
        remove_file('test.txt')


def test_get_local_datetime():
    dt_now = datetime.datetime.now()
    dt = dt_now.isoformat()
    dt_tz = get_local_datetime(dt)
    assert isinstance(get_local_datetime(dt), datetime.datetime)
    assert (dt_tz - dt_now) == datetime.timedelta(hours=TIMEZONE_HOURS_OFFSET)
