from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages import account_success_page
from pages.account_success_page import AccountSuccessPage


class registerPage:
    firstname = (By.XPATH, "//input[@id='input-firstname']")
    lastname = (By.XPATH, "//input[@id='input-lastname']")
    email = (By.XPATH, "//input[@id='input-email']")
    telephone = (By.XPATH, "//input[@id='input-telephone']")
    password = (By.XPATH, "//input[@id='input-password']")
    confirmPassword = (By.XPATH, "//input[@id='input-confirm']")
    newsLetter = (By.XPATH, "//input[@name='newsletter'][@value='1']")
    privacyPolicy = (By.NAME, "agree")
    continueBtn = (By.XPATH, "//input[@value='Continue']")

    # TC_RF_004
    firstname_warning = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
    lastname_warning = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
    email_warning = (By.XPATH, "//input[@id='input-email']/following-sibling::div")
    telephone_warning = (By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
    password_warning = (By.XPATH, "//input[@id='input-password']/following-sibling::div")
    privacy_policy_warning = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    # ==========================================================

    # TC_RF_008
    password_warning_message = (By.XPATH, "//input[@id='input-confirm']/following-sibling::div")
    # ==========================================================

    # TC_RF_009
    email_already_registered_warning = (By.XPATH,
                                        "//div[@class='alert alert-danger alert-dismissible'][text()='Warning: E-Mail Address is already registered!']")
    # ==========================================================

    # TC_RF_010
    invalid_email_warning_message = (By.XPATH, "//input[@type='email']/following-sibling::div")
    # ==========================================================

    # TC_RF_011
    invalid_telephone_warning_message = (By.XPATH, "//input[@type='telephone']/following-sibling::div")
    # ==========================================================
    # TC_RF_014
    first_name_label = (By.XPATH, "//label[@for='input-firstname']")
    last_name_label = (By.XPATH, "//label[@for='input-lastname']")
    email_label = (By.XPATH, "//label[@for='input-email']")
    telephone_label = (By.XPATH, "//label[@for='input-telephone']")
    password_label = (By.XPATH, "//label[@for='input-password']")
    confirm_password_label = (By.XPATH, "//label[@for='input-confirm']")
    # ==========================================================
    # TC_LG_006
    logout_display_right_column = (By.XPATH,
                                   "//aside[@id='column-right']//div[@class='list-group']//a[text()='Logout']")

    # ==========================================================

    def __init__(self, driver):
        self.driver = driver

    # TC_RF_001
    def enter_first_name(self, firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def enter_telephone(self, telephone):
        self.driver.find_element(*self.telephone).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)

    def enter_confirm_password(self, confirmPassword):
        self.driver.find_element(*self.confirmPassword).send_keys(confirmPassword)

    def selectNewsLetterOption(self):
        self.driver.find_element(*self.newsLetter).click()

    def selectedPrivacyPolicyField(self):
        self.driver.find_element(*self.privacyPolicy).click()

    def click_continue_btn(self):
        self.driver.find_element(*self.continueBtn).click()
        return AccountSuccessPage(self.driver)

    # ==========================================================

    # TC_RF_004
    def get_firstname_warning(self):
        try:
            return self.driver.find_element(*self.firstname_warning).text
        except NoSuchElementException:
            return ""

    def get_lastname_warning(self):
        try:
            return self.driver.find_element(*self.lastname_warning).text
        except NoSuchElementException:
            return ""

    def get_email_warning(self):
        try:
            return self.driver.find_element(*self.email_warning).text
        except NoSuchElementException:
            return ""

    def get_telephone_warning(self):
        try:
            return self.driver.find_element(*self.telephone_warning).text
        except NoSuchElementException:
            return ""

    def get_password_warning(self):
        try:
            return self.driver.find_element(*self.password_warning).text
        except NoSuchElementException:
            return ""

    def get_privacy_policy_warning(self):
        try:
            return self.driver.find_element(*self.privacy_policy_warning).text
        except NoSuchElementException:
            return ""

    # ==========================================================

    # TC_RF_008
    def get_password_warning_message(self):
        return self.driver.find_element(*self.password_warning_message).text

    # ==========================================================

    # TC_RF_009
    def get_email_already_registered_warning(self):
        return self.driver.find_element(*self.email_already_registered_warning).text

    # ==========================================================

    # TC_RF_010
    def get_invalid_email_warning_message(self):
        return self.driver.find_element(*self.invalid_email_warning_message).text

    def get_browser_validation_message(self):
        return self.driver.find_element(*self.email).get_attribute("validationMessage")

    # ==========================================================

    # TC_RF_010
    def get_telephone_warning_message(self):
        return self.driver.find_element(*self.invalid_telephone_warning_message).text

    # ==========================================================

    # TC_RF_013
    def get_firstname_placeholder(self):
        return self.driver.find_element(*self.firstname).get_attribute("placeholder")

    def get_lastname_placeholder(self):
        return self.driver.find_element(*self.lastname).get_attribute("placeholder")

    def get_email_placeholder(self):
        return self.driver.find_element(*self.email).get_attribute("placeholder")

    def get_telephone_placeholder(self):
        return self.driver.find_element(*self.telephone).get_attribute("placeholder")

    def get_password_placeholder(self):
        return self.driver.find_element(*self.password).get_attribute("placeholder")

    def get_confirm_password_placeholder(self):
        return self.driver.find_element(*self.confirmPassword).get_attribute("placeholder")

    # ==========================================================

    # TC_RF_014
    def get_first_name_label(self):
        return self.driver.find_element(*self.first_name_label).get_attribute("class")

    def get_last_name_label(self):
        return self.driver.find_element(*self.last_name_label).get_attribute("class")

    def get_email_label(self):
        return self.driver.find_element(*self.email_label).get_attribute("class")

    def get_telephone_label(self):
        return self.driver.find_element(*self.telephone_label).get_attribute("class")

    def get_password_label(self):
        return self.driver.find_element(*self.password_label).get_attribute("class")

    def get_confirm_password_label(self):
        return self.driver.find_element(*self.confirm_password_label).get_attribute("class")
    # ==========================================================

    # TC_LG_006
    def is_logout_display_right_column(self):
        try:
            return self.driver.find_element(*self.logout_display_right_column).is_displayed()
        except NoSuchElementException:
            return False

