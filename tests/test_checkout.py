import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data_loader import get_checkout_users, get_invalid_checkout_users


@pytest.fixture
def checkout(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.go_to_cart()
    cart = CartPage(page)
    cart.proceed_to_checkout()
    return CheckoutPage(page)


@pytest.mark.parametrize("first_name, last_name, zip_code", get_checkout_users())
def test_valid_checkout_completes(checkout, first_name, last_name, zip_code):
    checkout.fill_details(first_name, last_name, zip_code)
    checkout.continue_checkout()
    checkout.finish_checkout()
    assert "Thank you" in checkout.get_success_message()


@pytest.mark.parametrize("first_name, last_name, zip_code, expected_error", get_invalid_checkout_users())
def test_invalid_checkout_shows_error(checkout, first_name, last_name, zip_code, expected_error):
    checkout.fill_details(first_name, last_name, zip_code)
    checkout.continue_checkout()
    error = checkout.get_error_message()
    assert expected_error in error


def test_checkout_summary_shows_total(checkout):
    checkout.fill_details("John", "Doe", "12345")
    checkout.continue_checkout()
    total = checkout.get_total()
    assert "Total" in total