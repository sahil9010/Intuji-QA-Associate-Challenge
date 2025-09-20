from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class ProductDetailPage(BasePage):
    product_title = (By.CSS_SELECTOR, ".product-information h2")
    product_price = (By.CSS_SELECTOR, ".product-information span span")
    availability = (By.XPATH, "//b[contains(text(),'Availability')]")
    add_to_cart_btn = (By.CSS_SELECTOR, "button.cart")
    view_cart_btn = (By.CSS_SELECTOR, "a[href='/view_cart']")

    def get_product_info(self):
        title = self.get_text(self.product_title)
        price = self.get_text(self.product_price)
        available = self.get_text(self.availability)
        return {"title": title, "price": price, "availability": available}

    def add_to_cart(self):
        self.click(self.add_to_cart_btn)
        time.sleep(1)
        self.click(self.view_cart_btn)
        time.sleep(2)
