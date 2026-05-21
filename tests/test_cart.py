import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.test_data_loader import get_products


@pytest.fixture
def cart(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.go_to_cart()
    return CartPage(page)


def test_cart_contains_added_item(cart):
    names = cart.get_cart_item_names()
    assert "Sauce Labs Backpack" in names


def test_cart_item_count_is_correct(cart):
    assert cart.get_cart_item_count() == 1


def test_remove_item_from_cart(cart):
    cart.remove_item("Sauce Labs Backpack")
    assert cart.is_empty()


def test_cart_is_empty_after_removing_all(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.add_product_to_cart("Sauce Labs Bike Light")
    inventory.go_to_cart()
    cart = CartPage(page)
    cart.remove_item("Sauce Labs Backpack")
    cart.remove_item("Sauce Labs Bike Light")
    assert cart.is_empty()


def test_continue_shopping_returns_to_inventory(cart):
    cart.continue_shopping()
    assert "inventory" in cart.page.url