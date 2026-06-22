from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class basePage:
    def __init__(self, driver):
        self.driver = driver

    # click element
    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

   # get page title
    def get_page_title(self):
       return self.driver.title

   # navigate URL
    def open_url(self, url):
       self.driver.get(url)