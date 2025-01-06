import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


def pytest_report_header(config):
    return "TELEGARM BOT TESTS"