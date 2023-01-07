"""Test CSV Generator"""

from datagenie.csv_generator import get_fake_name


def test_fake_name():
    """Test fake name"""
    assert len(get_fake_name()) > 0
