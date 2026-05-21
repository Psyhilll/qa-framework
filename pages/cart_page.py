from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.cart_items = ".cart_item"
        self.cart_item_names = ".inventory_item_name"
        self.cart_item_prices = ".inventory_item_price"
        self.remove_buttons = "[data-test^='remove']"
        self.checkout_button = "[data-test='checkout']"
        self.continue_shopping_button = "[data-test='continue-shopping']"

    def get_cart_item_names(self):
        return self.page.locator(self.cart_item_names).all_text_contents()

    def get_cart_item_count(self):
        return self.page.locator(self.cart_items).count()

    def remove_item(self, product_name):
        self.page.locator(f".cart_item:has-text('{product_name}') button").click()

    def proceed_to_checkout(self):
        self.click(self.checkout_button)

    def continue_shopping(self):
        self.click(self.continue_shopping_button)

    def is_empty(self):
        return self.page.locator(self.cart_items).count() == 0