import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data_loader import get_sort_options, get_products


@pytest.fixture
def inventory(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    return InventoryPage(page)


@allure.feature("Inventory")
class TestInventory:

    @allure.story("Page Load")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_inventory_page_loads(self, inventory):
        with allure.step("Verify inventory URL"):
            assert "inventory" in inventory.page.url

    @allure.story("Product Display")
    @allure.severity(allure.severity_level.NORMAL)
    def test_inventory_shows_six_products(self, inventory):
        with allure.step("Get all product names"):
            names = inventory.get_product_names()
        with allure.step("Verify 6 products are shown"):
            assert len(names) == 6

    @allure.story("Sorting")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("sort_value", get_sort_options())
    def test_sort_products(self, inventory, sort_value):
        with allure.step(f"Sort by {sort_value}"):
            inventory.sort_by(sort_value)
        with allure.step("Verify sort order is correct"):
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

    @allure.story("Cart Actions")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("product_name", get_products())
    def test_add_product_to_cart(self, inventory, product_name):
        with allure.step(f"Add '{product_name}' to cart"):
            inventory.add_product_to_cart(product_name)
        with allure.step("Verify cart count is 1"):
            assert inventory.get_cart_count() == 1

    @allure.story("Cart Actions")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("product_name", get_products())
    def test_remove_product_from_cart(self, inventory, product_name):
        with allure.step(f"Add '{product_name}' to cart"):
            inventory.add_product_to_cart(product_name)
        with allure.step(f"Remove '{product_name}' from cart"):
            inventory.remove_product_from_cart(product_name)
        with allure.step("Verify cart is empty"):
            assert inventory.get_cart_count() == 0