from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

from pages.change_password_page import MyAccount_ChangePasswordPage
from pages.product_display_page import ProductDisplayPage


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    # TC_RF_001
    # ==========================================================
    edit_account_information_option = (By.LINK_TEXT, "Edit your account information")

    # TC_RF_005
    # ==========================================================
    subscribeUnscribeToNewsletterOption = (By.LINK_TEXT, "Subscribe / unsubscribe to newsletter")

    # ==========================================================
    # TC_LF_001
    check_logout_display = (By.XPATH, "//div[@class='list-group']//a[text()='Logout']")

    # ==========================================================
    # TC_LF_009
    check_my_account_title = (By.XPATH, "//div[@id='content']//h2[text()='My Account']")

    # ==========================================================
    # TC_LF_016
    change_password = (By.XPATH, "//ul[@class='list-unstyled']//a[text()='Change your password']")
    verify_account_ = (By.XPATH, "//ul[@class='breadcrumb']/li[2]")

    # ==========================================================
    # TC_LG_002
    my_account_right_side_bar_log_out = (By.XPATH,
                                         "//aside[@id='column-right']//div[@class='list-group']//a[text()='Logout']")

    # ==========================================================
    # TC_ATC_002
    search_product_xpath = (By.XPATH, "//input[@type='text']")
    search_product_button_xpath = (By.XPATH, "//div[@id='search']//button[@type='button']")

    # ==========================================================
    #TC_WL_003
    store_logo_link_text = (By.LINK_TEXT, "Qafox.com")


    # TC_RF_001
    # ==========================================================
    def did_we_navigate_to_my_account_page(self):
        return self.driver.find_element(*self.edit_account_information_option).is_displayed()

    # ==========================================================
    # TC_RF_005
    # ==========================================================
    def clickOnSubscribeUnscribeToNewsletterOption(self):
        self.driver.find_element(*self.subscribeUnscribeToNewsletterOption).click()

    # ==========================================================
    # TC_LF_001
    # ==========================================================
    def did_we_navigate_logout_to_my_account_page(self):
        return self.driver.find_element(*self.check_logout_display).is_displayed()

    # ==========================================================
    # TC_LF_009
    def did_we_navigate_my_account_page(self):
        return self.driver.find_element(*self.check_my_account_title).is_displayed()

    # ==========================================================
    # TC_LF_016
    def click_on_change_password(self):
        self.driver.find_element(*self.change_password).click()
        return MyAccount_ChangePasswordPage(self.driver)

    # ==========================================================
    # TC_LF_016
    def did_we_navigate_on_verify_account_breadcrumb(self):
        self.driver.find_element(*self.verify_account_).click()

    # ==========================================================
    # TC_LG_002
    def click_my_account_right_side_bar_log_out(self):
        self.driver.find_element(*self.my_account_right_side_bar_log_out).click()

    # ==========================================================
    # TC_ATC_002
    def enter_search_product_name(self, product_name):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.search_product_xpath)
            )
            search_box.clear()
            search_box.send_keys(product_name)
            return True
        except TimeoutException:
            return False

    def click_search_product_button(self):
        self.driver.find_element(*self.search_product_button_xpath).click()
        return ProductDisplayPage(self.driver)

    # ==========================================================
    # TC_WL_003
    def click_store_logo(self):
        try:
            store_logo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.store_logo_link_text)
            )
            store_logo.click()
        except (TimeoutException, StaleElementReferenceException):
            return False