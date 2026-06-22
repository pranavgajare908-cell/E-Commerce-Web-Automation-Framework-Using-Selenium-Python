import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions



def get_driver(browser):
    chrome_options = ChromeOptions()


    if browser == "chrome":
        browser = browser.lower()
        if os.getenv("JENKINS_HOME"):
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--remote-debugging-port=9222")
            chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()
            )
        )
    elif browser == "edge":
        driver = webdriver.Edge(
            service=EdgeService(
                EdgeChromiumDriverManager().install()
            )
        )
    else:
        raise Exception("Browser is not supported")

    driver.maximize_window()
    return driver
