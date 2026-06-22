from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(browser):

    browser = browser.lower()
    if browser == "chrome":
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
