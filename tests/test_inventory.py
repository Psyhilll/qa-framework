from pages.login_page import LoginPage


def test_inventory_items_visible(page):

    login = LoginPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    # Check inventory page loaded
    assert "inventory" in page.url

    # Check products are visible
    items = page.locator(".inventory_item")

    assert items.count() > 0