

from pages.login_page import LoginPage


def test_valid_login(page):

    login = LoginPage(page)

    login.open()

    login.login("standard_user", "secret_sauce")

    assert "inventory" in page.url


def test_invalid_login(page):

    login = LoginPage(page)

    login.open()

    login.login("wrong_user", "wrong_password")

    error = login.get_error_message()

    assert "Epic sadface" in error

def test_empty_login(page):

    login = LoginPage(page)

    login.open()
    login.login("", "")

    error = login.get_error_message()

    assert error is not None    