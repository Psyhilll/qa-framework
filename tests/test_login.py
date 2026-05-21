import pytest
from pages.login_page import LoginPage
from utils.test_data_loader import get_valid_users, get_invalid_users


@pytest.mark.parametrize("username, password, expected_url", get_valid_users())
def test_valid_login(page, username, password, expected_url):
    login = LoginPage(page)
    login.open()
    login.login(username, password)
    assert expected_url in page.url


@pytest.mark.parametrize("username, password, expected_error", get_invalid_users())
def test_invalid_login(page, username, password, expected_error):
    login = LoginPage(page)
    login.open()
    login.login(username, password)
    error = login.get_error_message()
    assert expected_error in error