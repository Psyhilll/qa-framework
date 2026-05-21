from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.first_name_field = "[data-test='firstName']"
        self.last_name_field = "[data-test='lastName']"
        self.zip_field = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"
        self.finish_button = "[data-test='finish']"
        self.error_message = "[data-test='error']"
        self.success_header = ".complete-header"
        self.summary_total = ".summary_total_label"

    def fill_details(self, first_name, last_name, zip_code):
        self.fill(self.first_name_field, first_name)
        self.fill(self.last_name_field, last_name)
        self.fill(self.zip_field, zip_code)

    def continue_checkout(self):
        self.click(self.continue_button)

    def finish_checkout(self):
        self.click(self.finish_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def get_success_message(self):
        return self.get_text(self.success_header)

    def get_total(self):
        return self.get_text(self.summary_total)