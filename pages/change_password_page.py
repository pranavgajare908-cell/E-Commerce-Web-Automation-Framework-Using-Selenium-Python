from selenium.webdriver.common.by import By


class MyAccount_ChangePasswordPage:
    def __init__(self, driver):
        self.driver = driver

    # ==========================================================
    # TC_LF_016
    change_password = (By.XPATH, "//input[@id='input-password']")
    confirm_password = (By.XPATH, "//input[@id='input-confirm']")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    change_password_success_message = (By.XPATH,
                                       "//div[contains(@class,'alert-success') and contains(text(),'Success: Your password has been successfully updated.')]")

    # ==========================================================
    # TC_LF_016
    def enter_change_password(self, change_password):
        return self.driver.find_element(*self.change_password).send_keys(change_password)

    def enter_confirm_password(self, confirm_password):
        return self.driver.find_element(*self.confirm_password).send_keys(confirm_password)

    def click_continue_button(self):
        return self.driver.find_element(*self.continue_button).click()

    def get_alert_change_password_success_message(self):
        return self.driver.find_element(*self.change_password_success_message).text
