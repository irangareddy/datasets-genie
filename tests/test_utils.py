"""test utils"""
import os
import pytest
from datagenie.utils import get_datagenie_env, get_file_location, generate_file_name


@pytest.fixture
def test_utils():
    """fixture for test utils"""
    os.environ['DATAGENIE_API_KEY'] = 'abc123'
    os.environ['DATAGENIE_DEBUG'] = 'True'
    yield
    del os.environ['DATAGENIE_API_KEY']
    del os.environ['DATAGENIE_DEBUG']


def test_get_file_location():
    """tests file location"""
    # Test default location
    assert get_file_location() != ''
    # Test location from function parameter
    assert get_file_location('.') == os.path.abspath('.')
    # Test non-existent location
    assert get_file_location('/nonexistent/path') is None
    # Test file instead of directory
    assert get_file_location('/path/to/file') is None


def test_generate_file_name():
    """tests generate file name"""
    # Test default file name
    assert generate_file_name(file_type='csv',
                              file_name=None).split('_')[0] == 'datagenie'
    # Test file name with extension
    assert generate_file_name('csv',
                              file_name='datagenie.csv') == 'datagenie.csv'


def test_get_datagenie_env(test_utils):
    """Check that the function returns the correct dictionary"""
    keys = get_datagenie_env()
    assert keys['DATAGENIE_API_KEY'] == 'abc123'
    assert keys['DATAGENIE_DEBUG'] == 'True'
