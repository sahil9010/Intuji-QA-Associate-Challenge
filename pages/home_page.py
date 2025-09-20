from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    signup_btn = (By.CSS_SELECTOR, "a[href='/login']")
    products_btn = (By.CSS_SELECTOR, "a[href='/products']")
    logout_btn = (By.CSS_SELECTOR, "a[href='/logout']")
    logged_in_label = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def go_to_signup(self):
        self.click(self.signup_btn)

    def go_to_products(self):
        self.click(self.products_btn)

    def logout(self):
        self.click(self.logout_btn)

    def is_logged_in(self):
        return self.is_visible(self.logged_in_label)
