import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_valid_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)

        login.open()
        login.login("standard_user", "secret_sauce")

        assert "inventory" in page.url

        browser.close()


def test_invalid_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)

        login.open()

        login.login("wrong_user", "wrong_password")

        error = login.get_error_message()

        assert "Epic sadface" in error

        browser.close()