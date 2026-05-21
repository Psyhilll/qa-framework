from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.sort_dropdown = "[data-test='product-sort-container']"
        self.product_names = ".inventory_item_name"
        self.product_prices = ".inventory_item_price"
        self.add_to_cart_buttons = ".btn_inventory"
        self.cart_badge = ".shopping_cart_badge"

    def get_product_names(self):
        return self.page.locator(self.product_names).all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator(self.product_prices).all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def sort_by(self, value):
        self.page.locator(self.sort_dropdown).select_option(value)

    def add_product_to_cart(self, product_name):
        self.page.locator(f".inventory_item:has-text('{product_name}') button").click()

    def remove_product_from_cart(self, product_name):
        self.page.locator(f".inventory_item:has-text('{product_name}') button").click()

    def get_cart_count(self):
        badge = self.page.locator(self.cart_badge)
        if badge.is_visible():
            return int(badge.text_content())
        return 0

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()