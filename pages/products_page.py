from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class ProductsPage(BasePage):
    women_toggle = (By.CSS_SELECTOR, "a[href='#Women']")
    women_dress = (By.CSS_SELECTOR, "a[href='/category_products/1']")
    product_name = (By.CSS_SELECTOR, ".features_items .productinfo p")
    first_product = (By.CSS_SELECTOR, ".features_items .productinfo a")

    def filter_women_dress(self):
        wait = WebDriverWait(self.driver, 10)
        self.click(self.women_toggle)  # expand women
        wait.until(EC.element_to_be_clickable(self.women_dress))
        self.click(self.women_dress)
        time.sleep(2)

    def get_product_names(self):
        return [el.text for el in self.driver.find_elements(*self.product_name)]

    def open_first_product(self):
        self.click(self.first_product)
        time.sleep(2)
