import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data_loader import get_sort_options, get_products


@pytest.fixture
def inventory(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    return InventoryPage(page)


def test_inventory_page_loads(inventory):
    assert "inventory" in inventory.page.url


def test_inventory_shows_six_products(inventory):
    names = inventory.get_product_names()
    assert len(names) == 6


@pytest.mark.parametrize("sort_value", get_sort_options())
def test_sort_products(inventory, sort_value):
    inventory.sort_by(sort_value)
    names = inventory.get_product_names()
    prices = inventory.get_product_prices()

    if sort_value == "az":
        assert names == sorted(names)
    elif sort_value == "za":
        assert names == sorted(names, reverse=True)
    elif sort_value == "lohi":
        assert prices == sorted(prices)
    elif sort_value == "hilo":
        assert prices == sorted(prices, reverse=True)


@pytest.mark.parametrize("product_name", get_products())
def test_add_product_to_cart(inventory, product_name):
    inventory.add_product_to_cart(product_name)
    assert inventory.get_cart_count() == 1


@pytest.mark.parametrize("product_name", get_products())
def test_remove_product_from_cart(inventory, product_name):
    inventory.add_product_to_cart(product_name)
    inventory.remove_product_from_cart(product_name)
    assert inventory.get_cart_count() == 0