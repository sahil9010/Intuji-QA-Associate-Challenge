from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    email_input = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    password_input = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    login_btn = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    def login(self, email, password):
        self.fill(self.email_input, email)
        self.fill(self.password_input, password)
        self.click(self.login_btn)
        time.sleep(2)  # wait for login to complete
