import pytest
import allure
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


@allure.feature("Checkout")
class TestCheckout:

    @allure.story("Valid Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("first_name, last_name, zip_code", get_checkout_users())
    def test_valid_checkout_completes(self, checkout, first_name, last_name, zip_code):
        with allure.step(f"Fill checkout details for {first_name} {last_name}"):
            checkout.fill_details(first_name, last_name, zip_code)
            checkout.continue_checkout()
        with allure.step("Complete purchase"):
            checkout.finish_checkout()
        with allure.step("Verify success message"):
            assert "Thank you" in checkout.get_success_message()

    @allure.story("Invalid Checkout")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("first_name, last_name, zip_code, expected_error", get_invalid_checkout_users())
    def test_invalid_checkout_shows_error(self, checkout, first_name, last_name, zip_code, expected_error):
        with allure.step("Fill incomplete checkout details"):
            checkout.fill_details(first_name, last_name, zip_code)
            checkout.continue_checkout()
        with allure.step("Verify error message"):
            error = checkout.get_error_message()
            assert expected_error in error

    @allure.story("Order Summary")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_summary_shows_total(self, checkout):
        with allure.step("Fill valid details and continue"):
            checkout.fill_details("John", "Doe", "12345")
            checkout.continue_checkout()
        with allure.step("Verify total is displayed"):
            total = checkout.get_total()
            assert "Total" in total