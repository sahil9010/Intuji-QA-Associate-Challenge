import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()
        time.sleep(1)

    def fill(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
        time.sleep(1)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def is_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()
