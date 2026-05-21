from pages.login_page import LoginPage


def test_add_item_to_cart(page):

    login = LoginPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    # Add item to cart
    page.click("#add-to-cart-sauce-labs-backpack")

    # Go to cart
    page.click(".shopping_cart_link")

    # Verify item in cart
    cart_items = page.locator(".cart_item")

    assert cart_items.count() == 1