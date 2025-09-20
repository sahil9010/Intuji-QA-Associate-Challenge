from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage

class RegisterPage(BasePage):
    # Step 1 (signup form)
    name_input = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    email_input = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    signup_btn = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    # Step 2 (account info form)
    title_mr = (By.ID, "id_gender1")
    password_input = (By.ID, "password")
    days = (By.ID, "days")
    months = (By.ID, "months")
    years = (By.ID, "years")
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    address = (By.ID, "address1")
    country = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile = (By.ID, "mobile_number")
    create_account_btn = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    # Step 3 confirmation
    account_created_msg = (By.XPATH, "//b[text()='Account Created!']")
    continue_btn = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def register(self, user):
        wait = WebDriverWait(self.driver, 15)

        # Fill signup form
        self.fill(self.name_input, user["name"])
        self.fill(self.email_input, user["email"])
        self.click(self.signup_btn)

        # Wait for account info form
        wait.until(EC.visibility_of_element_located(self.password_input))

        # Fill mandatory fields
        self.click(self.title_mr)
        self.fill(self.password_input, user["password"])
        self.driver.find_element(*self.days).send_keys("1")
        self.driver.find_element(*self.months).send_keys("January")
        self.driver.find_element(*self.years).send_keys("2000")
        self.fill(self.first_name, user["name"])
        self.fill(self.last_name, "Test")
        self.fill(self.address, user["address"])
        self.driver.find_element(*self.country).send_keys("India")
        self.fill(self.state, user["state"])
        self.fill(self.city, user["city"])
        self.fill(self.zipcode, user["zipcode"])
        self.fill(self.mobile, user["phone"])

        self.click(self.create_account_btn)

        # Wait for confirmation
        wait.until(EC.visibility_of_element_located(self.account_created_msg))

        # Click Continue
        wait.until(EC.element_to_be_clickable(self.continue_btn)).click()
        time.sleep(2)
