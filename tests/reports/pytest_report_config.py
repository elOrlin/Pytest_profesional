import pytest

def pytest_configure(config):
    config.option.verbose = 2
    config.option.tbstyle = "short"
    config.option.capture = "no"
