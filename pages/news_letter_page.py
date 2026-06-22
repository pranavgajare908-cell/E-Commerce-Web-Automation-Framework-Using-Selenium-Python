from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewsLetterOption:
    def __init__(self, driver):
        self.driver = driver

    # ==========================================================
    # TC_RF_005
    # ==========================================================
    newsletterOption=(By.XPATH, "//input[@name='newsletter'][@value='1']")

    # ==========================================================
    # TC_RF_006
    # ==========================================================
    newsletterOption_NO=(By.XPATH, "//input[@name='newsletter'][@value='0']")

    # ==========================================================
    # TC_RF_005
    # ==========================================================
    def isNewsletterOption(self):
        return self.driver.find_element(*self.newsletterOption).is_selected()

    # ==========================================================
    # TC_RF_006
    # ==========================================================
    def isNewsletterOption_NO(self):
        return self.driver.find_element(*self.newsletterOption_NO).is_selected()