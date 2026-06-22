from selenium.webdriver.common.by import By
from pages.home_page import home_page


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    # TC_LG_001
    account_log_out_breadcrumb = (By.XPATH, "//ul[@class='breadcrumb']//a[text()='Logout']")
    log_out_continue_button = (By.LINK_TEXT, "Continue")

    # ==========================================================

    # TC_LG_001
    def get_account__log_out_breadcrumb(self):
        return self.driver.find_element(*self.account_log_out_breadcrumb).is_displayed()

    def click_log_out_continue_button(self):
         self.driver.find_element(*self.log_out_continue_button).click()
         return home_page(self.driver)
