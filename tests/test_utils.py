import pytest

from utils import remove_file


def test_remove_file():
    with pytest.raises(FileNotFoundError):
        remove_file('test.txt')
