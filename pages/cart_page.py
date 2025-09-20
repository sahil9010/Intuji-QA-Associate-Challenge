import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    quantity_input = (By.CSS_SELECTOR, "input.cart_quantity_input")
    remove_btn = (By.CLASS_NAME, "cart_quantity_delete")
    checkout_btn = (By.CSS_SELECTOR, "a.check_out")

    def change_quantity(self, qty):
        elem = self.driver.find_element(*self.quantity_input)
        elem.clear()
        elem.send_keys(str(qty))
        elem.send_keys("\n")
        time.sleep(2)

    def remove_item(self):
        self.click(self.remove_btn)

    def go_to_checkout(self):
        self.click(self.checkout_btn)
