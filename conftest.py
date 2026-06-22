import os
import time

import pytest

from utilities.driver_factory import get_driver
from utilities.read_properties import ReadConfig
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.screenshot import CaptureScrenshot
import pytest_html


# ==========================================================
# HTML Report Configuration
# ==========================================================
def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Prooject Name"] = (
            "E-Commerce Automation Framework"
        )
        config._metadata["Tester"] = (
            "Pranav Gajare"
        )
        config._metadata["Framework"] = (
            "Pytest + Selenium + POM"
        )
        config._metadata["Browser"] = (
            ReadConfig.get_browser()
        )


def pytest_html_report_title(report):
    report.title = (
        "Automation Framework"
    )


# ==========================================================
# Browser Option
# ==========================================================
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption(
        "--browser"
    )


# ==========================================================
# Browser Setup Fixture
# ==========================================================
@pytest.fixture()
def setup(request):
    browser = ReadConfig.get_browser()

    driver = get_driver(browser)

    yield driver

    #driver.quit()


# ==========================================================
# Persistent Browser Session Fixture
# Used for Session/Cookie related Test Cases
# ==========================================================
@pytest.fixture()
def setup_persistence():
    browser = ReadConfig.get_browser().lower()
    # Browser-specific profile folder
    profile_path = os.path.join(
        os.getcwd(),
        "ChromeAutomationProfile"
    )
    print(profile_path)
    os.makedirs(profile_path, exist_ok=True)
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument(f"--user-data-dir={profile_path}")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--profile-directory=Default")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=options)
        # driver.get("https://google.com")
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument(f"--user-data-dir={profile_path}")
        driver = webdriver.Edge(options=options)
    else:
        raise Exception(f"Browser '{browser}' is not supported")
    driver.maximize_window()
    yield driver
    driver.quit()


# # ==========================================================
# # Capture Screenshot Automatically On Test Failure
# # ==========================================================
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call":
#         extra = getattr(report, "extras", [])
#         if report.failed:
#             driver = None
#             if "setup" in item.funcargs:
#                 driver = item.funcargs["setup"]
#             elif "setup_persistence" in item.funcargs:
#                 driver = item.funcargs["setup_persistence"]
#             if driver:
#                 screenshot_path = (
#                     CaptureScrenshot.capture_screenshot(
#                         driver,
#                         f"Failed_{item.name}"
#                     )
#                 )
#                 pytest_html = item.config.pluginmanager.getplugin("html")
#                 if pytest_html:
#                     extra.append(
#                         pytest_html.extras.image(
#                             screenshot_path,
#                             mime_type="image/png"
#                         )
#                     )
#                 report.extras = extra
#                 print(
#                     f"\nScreenshot Captured: "
#                     f"{screenshot_path}"
#                 )