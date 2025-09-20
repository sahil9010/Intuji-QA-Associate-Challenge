from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    place_order_btn = (By.CSS_SELECTOR, "a[href='/payment']")
    name_on_card = (By.NAME, "name_on_card")
    card_number = (By.NAME, "card_number")
    cvc = (By.NAME, "cvc")
    exp_month = (By.NAME, "expiry_month")
    exp_year = (By.NAME, "expiry_year")
    pay_btn = (By.CSS_SELECTOR, "button[data-qa='pay-button']")
    confirmation_msg = (By.XPATH, "//p[contains(text(),'Your order has been placed successfully!')]")

    def place_order(self, user):
        self.click(self.place_order_btn)
        self.fill(self.name_on_card, user["name"])
        self.fill(self.card_number, "4111111111111111")
        self.fill(self.cvc, "123")
        self.fill(self.exp_month, "12")
        self.fill(self.exp_year, "2026")
        self.click(self.pay_btn)

    def is_order_successful(self):
        return self.is_visible(self.confirmation_msg)
