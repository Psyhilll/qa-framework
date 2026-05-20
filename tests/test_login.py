from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.fill("#user-name", "standard_user")

        page.fill("#password", "secret_sauce")

        page.click("#login-button")

        assert "inventory" in page.url

        browser.close()