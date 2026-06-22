from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.my_account_page import MyAccountPage


class AccountSuccessPage:

    def __init__(self, driver):
        self.driver = driver

    success_message_one = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
    success_message_two = (By.XPATH, "//div[@id='content']/p[1]")
    success_message_three = (By.XPATH, "//div[@id='content']/p[2]")
    success_message_four = (By.XPATH, "//div[@id='content']/p[3]")
    success_message_five = (By.XPATH, "//div[@id='content']/p[4]")
    log_out_option = (By.XPATH, "//a[@class='list-group-item'][text()='Logout']")
    account_success_page = (By.XPATH, "//ul[@class='breadcrumb']//a[text()='Success']")
    success_continue_button = (By.LINK_TEXT, "Continue")

    # ==========================================================
    # TC_RF_012
    display_logout_button=(By.XPATH, "//div[@class='list-group']//a[text()='Logout']")
    # ==========================================================

    def get_success_message_one(self):
        return self.driver.find_element(*self.success_message_one).text

    def get_success_message_two(self):
        return self.driver.find_element(*self.success_message_two).text

    def get_success_message_three(self):
        return self.driver.find_element(*self.success_message_three).text

    def get_success_message_four(self):
        return self.driver.find_element(*self.success_message_four).text

    def get_success_message_five(self):
        return self.driver.find_element(*self.success_message_five).text

    def is_user_looged_in(self):
        return self.driver.find_element(*self.log_out_option).is_displayed()

    def is_account_successful(self):
        return self.driver.find_element(*self.account_success_page).is_displayed()

    def click_on_continue_button(self):
        self.driver.find_element(*self.success_continue_button).click()

        return MyAccountPage(self.driver)

    # ==========================================================
    # TC_RF_012
    def check_display_logout_button(self):
        return self.driver.find_element(*self.display_logout_button).is_displayed()
    # ==========================================================
