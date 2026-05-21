from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def open(self):
        self.goto("https://www.saucedemo.com")

    def login(self, user, pwd):
        self.fill(self.username, user)
        self.fill(self.password, pwd)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)