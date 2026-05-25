import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def cart(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.go_to_cart()
    return CartPage(page)


@allure.feature("Cart")
class TestCart:

    @allure.story("Cart Contents")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_contains_added_item(self, cart):
        with allure.step("Get cart item names"):
            names = cart.get_cart_item_names()
        with allure.step("Verify backpack is in cart"):
            assert "Sauce Labs Backpack" in names

    @allure.story("Cart Contents")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_item_count_is_correct(self, cart):
        with allure.step("Verify cart has 1 item"):
            assert cart.get_cart_item_count() == 1

    @allure.story("Remove Items")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_item_from_cart(self, cart):
        with allure.step("Remove backpack from cart"):
            cart.remove_item("Sauce Labs Backpack")
        with allure.step("Verify cart is empty"):
            assert cart.is_empty()

    @allure.story("Remove Items")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_is_empty_after_removing_all(self, page):
        with allure.step("Login and add two products"):
            login = LoginPage(page)
            login.open()
            login.login("standard_user", "secret_sauce")
            inventory = InventoryPage(page)
            inventory.add_product_to_cart("Sauce Labs Backpack")
            inventory.add_product_to_cart("Sauce Labs Bike Light")
            inventory.go_to_cart()
        with allure.step("Remove all items"):
            cart = CartPage(page)
            cart.remove_item("Sauce Labs Backpack")
            cart.remove_item("Sauce Labs Bike Light")
        with allure.step("Verify cart is empty"):
            assert cart.is_empty()

    @allure.story("Navigation")
    @allure.severity(allure.severity_level.MINOR)
    def test_continue_shopping_returns_to_inventory(self, cart):
        with allure.step("Click continue shopping"):
            cart.continue_shopping()
        with allure.step("Verify redirect to inventory"):
            assert "inventory" in cart.page.url