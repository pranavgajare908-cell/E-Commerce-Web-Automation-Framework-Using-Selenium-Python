from selenium.webdriver.common.by import By
from webdriver_manager.core import driver


class forgot_password_Page:
    def __init__(self, driver):
        self.driver = driver

    # ----------------------------------------
    # TC_LF_006
    navigate_to_forgot_password_page = (By.XPATH, "//ul[@class='breadcrumb']//a[text()='Forgotten Password']")

    # ----------------------------------------
    # TC_LF_006
    def did_we_navigate_to_forgotten_password_page(self):
        return self.driver.find_element(*self.navigate_to_forgot_password_page).is_displayed()
