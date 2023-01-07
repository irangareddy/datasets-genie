"""Test Faker Utils"""
import pytest
from datagenie.faker_utils import (
    callable_methods,
    get_callable_method_names,
    random_faker_method
)


@pytest.fixture()
def methods():
    """get methods"""
    return ['name', 'address', 'email', 'company', 'profile', 'phone_number']


def test_callable_methods_returns_list_of_strings(methods):
    """test_callable_methods_returns_list_of_strings"""
    result = callable_methods(methods)
    assert isinstance(result, list)
    assert len(result) == len(methods)


def test_random_faker_method_returns_string():
    """test_random_faker_method_returns_string"""
    result = random_faker_method()
    assert isinstance(result, str)


def test_get_callable_method_names_returns_list_of_strings():
    """test_get_callable_method_names_returns_list_of_strings"""
    result = get_callable_method_names()
    assert isinstance(result, list)
    assert all(isinstance(item, str) for item in result)
