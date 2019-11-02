"""
A simple example of using a json file to paramaterize tests.
"""
import json
import pytest

from example import greeter

TEST_DATA_LOCATION = "test-data.json"


def id_func(item: dict) -> str:
    """ Returns a unique id for each test, just make testing clear """
    return item["input"]


def pytest_generate_tests(metafunc):
    """ Reads in a json file and creates a 'test-case' fixture. """
    if "test_case" in metafunc.fixturenames:
        with open(TEST_DATA_LOCATION) as test_data_f:
            test_cases = json.load(test_data_f)
            metafunc.parametrize("test_case", [i for i in test_cases], ids=id_func)


def test_greeter(test_case):
    """ Do we introduce customers correctly? """
    assert greeter(test_case["input"]) == test_case["output"]
