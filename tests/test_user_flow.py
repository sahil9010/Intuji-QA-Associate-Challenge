import time
import pytest
from selenium import webdriver
from utils.faker_data import get_user_data
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver_init")
class TestUserFlow:
    def test_full_flow(self):
        user = get_user_data()

        driver = self.driver
        driver.get("https://automationexercise.com")
        driver.maximize_window()
        time.sleep(2)

        # Home
        home = HomePage(driver)
        home.go_to_signup()

        # Register
        register = RegisterPage(driver)
        register.register(user)
        assert home.is_logged_in()

        # Product Filtering
        products = ProductsPage(driver)
        home.go_to_products()
        products.filter_women_dress()
        names = products.get_product_names()
        assert any("Dress" in n for n in names)

        # Product Detail
        products.open_first_product()
        detail = ProductDetailPage(driver)
        title = detail.get_product_title()
        assert title is not None
        detail.add_to_cart()

        # Cart
        cart = CartPage(driver)
        cart.change_quantity(3)
        cart.go_to_checkout()

        # Checkout
        checkout = CheckoutPage(driver)
        checkout.place_order(user)
        assert checkout.is_order_successful()

        # Logout and Re-login
        home.logout()
        home.go_to_signup()
        driver.find_element("css selector", "input[data-qa='login-email']").send_keys(user["email"])
        driver.find_element("css selector", "input[data-qa='login-password']").send_keys(user["password"])
        driver.find_element("css selector", "button[data-qa='login-button']").click()
        time.sleep(2)
        assert home.is_logged_in()
