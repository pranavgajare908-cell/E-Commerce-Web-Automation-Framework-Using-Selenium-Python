

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.shopping_cart_page import ShoppingCartPage


class ShowAllProductsPage:
    def __init__(self, driver):
        self.driver = driver

    # TC_ATC_005
    # ==========================================================
    product_sub_categories_xpath = (By.XPATH, "//aside[@id='column-left']//a[3]")
    product_sub_categories_add_to_cart_xpath = (By.XPATH, "//button[@type='button']//span[text()='Add to Cart']")
    add_to_cart_success_message = (By.XPATH, "//ul[@class='breadcrumb']/following-sibling::div[1]")
    shopping_cart_xpath = (By.LINK_TEXT, "shopping cart")

    # TC_ATC_005
    # ==========================================================
    def click_product_sub_categories(self):
        self.driver.find_element(*self.product_sub_categories_xpath).click()

    def click_product_sub_categoies_add_to_cart(self):
        self.driver.find_element(*self.product_sub_categories_add_to_cart_xpath).click()

    def get_add_to_cart_success_message(self):
        return self.driver.find_element(*self.add_to_cart_success_message).is_displayed()

    def click_shopping_cart(self):
        try:
            shopping_cart = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.shopping_cart_xpath)
            )
            shopping_cart.click()
            return ShoppingCartPage(self.driver)
        except (TimeoutError,NoSuchElementException):
            return False