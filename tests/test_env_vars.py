import pytest
from os import environ

from env_vars import get_env_var

environ["EXISTED_VAR"] = "EXISTED_VAR"


def test_env_vars_1():
    with pytest.raises(ValueError):
        get_env_var("NOT_EXISTED_VAR")


def test_env_vars_2():
    assert get_env_var("EXISTED_VAR") == "EXISTED_VAR"
