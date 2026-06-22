import pytest
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import basePage
from pages.search_page import SearchPage
from pages.show_all_products import ShowAllProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.product_wishlist_page import WishlistPage


class home_page(basePage):
    lnk_myaccount_xpath = (By.XPATH, "//span[text()='My Account']")
    lnk_register_xpath = (By.XPATH, "//a[text()='Register']")
    lnk_login_xpath = (By.XPATH, "//a[text()='Login']")
    lnk_logout_xpath = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[text()='Logout']")
    home_page_title_xpath = (By.LINK_TEXT, "Qafox.com")
    search_product_xpath = (By.XPATH, "//input[@type='text']")
    search_product_button_xpath = (By.XPATH, "//span[@class='input-group-btn']//button[@type='button']")
    search_placeholder_xpath = (By.XPATH, "//input[@placeholder='Search']")
    hover_menu_desktop_link_text = (By.LINK_TEXT, "Desktops")
    show_all_desktop_link_text = (By.LINK_TEXT, "Show AllDesktops")

    products_feature_name_xpath = (
        By.XPATH,
        "//div[contains(@class,'product-thumb')]//h4/a"
    )
    product_feature_add_to_cart_xpath = (By.XPATH,
                                         "//div[contains(@class, 'product-thumb')]//div[@class='button-group']")

    add_to_cart_success_message_xpath = (By.XPATH, "//ul[@class='breadcrumb']/following-sibling::div[1]")

    shopping_cart_xpath = (By.LINK_TEXT, "shopping cart")

    product_wish_list_xpath = (By.XPATH, "//div[@class='button-group']//i[@class='fa fa-heart']")

    add_wish_list_success_message_xpath = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    wish_list_link_text = (By.LINK_TEXT, "wish list")

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        return self.driver.find_element(*self.lnk_myaccount_xpath).click()

    def click_registration(self):
        return self.driver.find_element(*self.lnk_register_xpath).click()

    def click_login(self):
        return self.driver.find_element(*self.lnk_login_xpath).click()

    def is_logout_displayed(self):
        try:
            return self.driver.find_element(*self.lnk_logout_xpath).is_displayed()
        except:
            return False

    def click_logout(self):
        try:
            return self.driver.find_element(*self.lnk_logout_xpath).click()
        except:
            return ""

    def get_home_page_title(self):
        return self.driver.find_element(*self.home_page_title_xpath).is_displayed()

    def enter_product_name(self, productName):
        self.driver.find_element(*self.search_product_xpath).send_keys(productName)

    def click_search_product(self):
        self.driver.find_element(*self.search_product_button_xpath).click()
        return SearchPage(self.driver)

    def get_search_placeholder(self):
        return self.driver.find_element(*self.search_placeholder_xpath).get_attribute("placeholder")

    def click_hover_desktop_menu(self):
        desktop = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.hover_menu_desktop_link_text)
        )
        ActionChains(self.driver).move_to_element(desktop).perform()

    def click_show_all_desktops(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.show_all_desktop_link_text)
        ).click()
        return ShowAllProductsPage(self.driver)

    def get_products_feature_name(self):
        elements = self.driver.find_elements(*self.products_feature_name_xpath)
        return [element.text.strip() for element in elements]

    def click_product_feature_add_to_cart(self):
        return self.driver.find_elements(*self.product_feature_add_to_cart_xpath)

    def get_add_to_cart_success_message(self):
        try:
            return self.driver.find_element(*self.add_to_cart_success_message_xpath).is_displayed()
        except NoSuchElementException:
            return False

    def click_add_to_cart(self):
        try:
            shopping_cart = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.shopping_cart_xpath)
            )
            shopping_cart.click()
            return ShoppingCartPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            return False

    def click_product_wish_list(self):
        return self.driver.find_elements(*self.product_wish_list_xpath)

    def get_add_wish_list_success_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.add_wish_list_success_message_xpath
            )
        )
        return element.text

    def click_wish_list_add_to_cart(self):
        try:
            wish_list = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.wish_list_link_text)
            )
            wish_list.click()
            return WishlistPage(self.driver)
        except (TimeoutException, NoSuchElementException):
            return False
