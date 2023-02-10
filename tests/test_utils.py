"""test utils"""
import os
import logging
import pytest
from datasets_genie.utils import (
    get_datasets_genie_env,
    get_file_location,
    generate_file_name,
    logger,
)


@pytest.fixture
def test_utils():
    """fixture for test utils"""
    os.environ["DATASETS_GENIE_API_KEY"] = "abc123"
    os.environ["DATASETS_GENIE_DEBUG"] = "True"
    yield
    del os.environ["DATASETS_GENIE_API_KEY"]
    del os.environ["DATASETS_GENIE_DEBUG"]


def test_get_file_location():
    """tests file location"""
    # Test default location
    assert get_file_location() != ""
    # Test location from function parameter
    assert get_file_location(".") == os.path.abspath(".")
    # Test non-existent location
    assert get_file_location("/nonexistent/path") is None
    # Test file instead of directory
    assert get_file_location("/path/to/file") is None


def test_generate_file_name():
    """tests generate file name"""
    # Test default file name
    assert (
        generate_file_name(file_type="csv", file_name=None).split("_")[0]
        == "datasets-genie"
    )
    # Test file name with extension
    assert (
        generate_file_name("csv", file_name="datasets-genie.csv")
        == "datasets-genie.csv"
    )


def test_get_datagenie_env(test_utils):
    """Check that the function returns the correct dictionary"""
    keys = get_datasets_genie_env()
    assert keys["DATASETS_GENIE_API_KEY"] == "abc123"
    assert keys["DATASETS_GENIE_DEBUG"] == "True"


def test_logger():
    """test log message"""
    value = "Test log message"
    # Test debug log level
    logger(value, debug=True)
    log_output = logging.getLogger().level
    assert log_output == 10

    # Test info log level
    logger(value, info=True)
    log_output = logging.getLogger().level
    assert log_output == 20

    # Test error log level
    logger(value, error=True)
    log_output = logging.getLogger().level
    assert log_output == 40
