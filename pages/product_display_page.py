from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pages.shopping_cart_page import ShoppingCartPage
from pages.product_wishlist_page import WishlistPage


class ProductDisplayPage:
    def __init__(self, driver):
        self.driver = driver

    # ----------------------------------------
    # TC_ATC_001
    add_to_cart_xpath = (By.XPATH, "//div[@class='button-group']//button//span[text()='Add to Cart']")
    add_to_cart_success_message_xpath = (By.XPATH, "//ul[@class='breadcrumb']/following-sibling::div[1]")
    shopping_cart_xpath = (By.LINK_TEXT, "shopping cart")

    # ----------------------------------------
    # TC_ATC_002
    wishlist_button_xpath = (By.XPATH, "//div[@class='product-thumb']//i[@class='fa fa-heart']")
    wishlist_header_xpath = (By.XPATH, "//a[@id='wishlist-total']//span[@class='hidden-xs hidden-sm hidden-md']")

    # ----------------------------------------
    # TC_ATC_003
    cart_button_xpath = (By.XPATH, "//div[@class='col-sm-3']//div[@id='cart']")
    view_cart_xpath = (By.XPATH,
                       "//ul[@class='dropdown-menu pull-right']//li//table[@class='table table-bordered']/following-sibling::p//a//strong[text()='View Cart']")

    # ----------------------------------------
    # TC_WL_002
    wish_list_xpath = (By.XPATH, "//div[@class='product-thumb']//i[@class='fa fa-heart']")
    wish_list_success_message_xpath = (By.XPATH, "//ul[@class='breadcrumb']/following-sibling::div[1]")
    wish_list_link_text = (By.LINK_TEXT, "wish list")

    # ----------------------------------------
    # TC_ATC_001
    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_xpath).click()

    def get_add_to_cart_success_message(self):
        return self.driver.find_element(*self.add_to_cart_success_message_xpath).is_displayed()

    def click_shopping_cart(self):
        try:
            shopping_cart = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.shopping_cart_xpath)
            )
            shopping_cart.click()
            return ShoppingCartPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            return False

    # ----------------------------------------
    # TC_ATC_002
    def click_product_wishlist(self):
        self.driver.find_element(*self.wishlist_button_xpath).click()

    def click_wishlist_header(self):
        self.driver.find_element(*self.wishlist_header_xpath).click()
        return WishlistPage(self.driver)

    # ----------------------------------------
    # TC_ATC_003
    def click_cart_button(self):
        self.driver.find_element(*self.cart_button_xpath).click()

    def click_view_cart(self):
        try:
            view_cart = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.view_cart_xpath)
            )
            view_cart.click()
            return ShoppingCartPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            return False

    # ----------------------------------------
    # TC_WL_002
    def click_wishlist(self):
        self.driver.find_element(*self.wishlist_button_xpath).click()

    def get_wishlist_success_message(self):
        return self.driver.find_element(*self.wish_list_success_message_xpath).is_displayed()

    def click_wishlist_link(self):
        try:
            wishlist_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.wish_list_link_text)
            )
            wishlist_link.click()
            return WishlistPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            return False
