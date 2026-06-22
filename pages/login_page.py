from selenium.webdriver.common.by import By

from pages.forgot_password_page import forgot_password_Page
from pages.my_account_page import MyAccountPage


class loginPage:
    # ----------------------------------------
    # TC_LF_001
    e_Mail_Address = (By.XPATH, "//input[@id='input-email']")
    e_Password = (By.XPATH, "//input[@id='input-password']")
    login_button = (By.XPATH, "//input[@type='submit']")

    # ----------------------------------------
    # TC_LF_002
    login_warning_message = (By.XPATH,
                             "//div[@class='alert alert-danger alert-dismissible'][text()='Warning: No match for E-Mail Address and/or Password.']")

    # ----------------------------------------
    # TC_LF_006
    forgotten_password = (By.XPATH, "//div[@class='form-group']//a[text()='Forgotten Password']")

    # ----------------------------------------
    # TC_LF_019
    new_customer_continue_Button = (By.XPATH, "//a[text()='Continue']")
    right_side_bar_register_page_link = (By.XPATH, "//div[@class='list-group']//a[text()='Register']")

    def __init__(self, driver):
        self.driver = driver

    # ----------------------------------------
    # TC_LF_001
    def enter_e_mail_address(self, email_address):
        self.driver.find_element(*self.e_Mail_Address).send_keys(email_address)

    def enter_password(self, password):
        self.driver.find_element(*self.e_Password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
        return MyAccountPage(self.driver)

    # ----------------------------------------
    # TC_LF_002
    def get_login_warning_message(self):
        return self.driver.find_element(*self.login_warning_message).text

    # ----------------------------------------
    # TC_LF_006
    def click_forgotten_password(self):
        self.driver.find_element(*self.forgotten_password).click()
        return forgot_password_Page(self.driver)

    # ----------------------------------------
    # TC_LF_008
    def get_email_field_placeholder(self):
        return self.driver.find_element(*self.e_Mail_Address).get_attribute("placeholder")

    def get_password_field_placeholder(self):
        return self.driver.find_element(*self.e_Password).get_attribute("placeholder")

    # ----------------------------------------
    # TC_LF_0013
    def get_password_field_type(self):
        return self.driver.find_element(*self.e_Password).get_attribute("type")

    # ----------------------------------------
    # TC_LF_002
    def get_clear_password_field_type(self):
        return self.driver.find_element(*self.e_Password).clear()

    # ----------------------------------------
    # TC_LF_019
    def click_on_new_customer_continue_button(self):
        self.driver.find_element(*self.new_customer_continue_Button).click()

    def click_right_side_bar_register_page_link(self):
        self.driver.find_element(*self.right_side_bar_register_page_link).click()
