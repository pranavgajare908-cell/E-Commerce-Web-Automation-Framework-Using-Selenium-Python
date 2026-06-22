import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.logger import logGen
from utilities.read_properties import ReadConfig
from pages.home_page import home_page
from pages.login_page import loginPage
from pages.logout_page import LogoutPage
from pages.my_account_page import MyAccountPage
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from pages.registration_page import registerPage

from utilities.screenshot import CaptureScrenshot


class TestLogOut:
    logger = logGen.logger()

    # ==========================================================
    # TC_LG_001
    # Verify Logging out by selecting Logout
    # option from 'My Account' dropmenu
    # ==========================================================
    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_logout_from_my_account_dropdown(self, setup):
        self.logger.info("========== TC_LG_001 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
        self.login_page.enter_password("1234")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("User Logged In Successfully")
        # ------------------------------------------------------
        # Click Logout
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        time.sleep(2)
        self.homepage.click_my_account()
        self.homepage.click_logout()
        self.logger.info("Clicked Logout Option")

        self.log_out_page = LogoutPage(self.driver)
        # ------------------------------------------------------
        # Validate Account Logout Heading
        # ------------------------------------------------------
        time.sleep(2)
        if self.log_out_page.get_account__log_out_breadcrumb():
            self.logger.info("Logout Successful")
        # ------------------------------------------------------
        # Click Logout Continue Button
        # ------------------------------------------------------
        self.log_out_page.click_log_out_continue_button()
        self.logger.info("Clicked On Logout Page")
        # ------------------------------------------------------
        # Verify the homepage title
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        time.sleep(2)
        if self.homepage.get_home_page_title():
            self.logger.info("Navigate to Homepage Successfully")
        self.logger.info("User should be taken to the Home page")
        self.logger.info("========== TC_LG_001 Passed ==========")

    # ==========================================================
    # TC_LG_002
    # Verify Logging out by selecting Logout option
    # from Right Column options
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_logout_from_right_column(self, setup):
        self.logger.info("========== TC_LG_002 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
        self.login_page.enter_password("1234")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("User Logged In Successfully")
        # ------------------------------------------------------
        self.my_account_page = MyAccountPage(self.driver)
        # ------------------------------------------------------
        # Click on Right Side Bar Log Out Button
        # ------------------------------------------------------
        self.my_account_page.click_my_account_right_side_bar_log_out()
        self.logger.info("Clicked On Logout Page")
        self.log_out_page = LogoutPage(self.driver)
        # ------------------------------------------------------
        # Validate Account Logout Heading
        # ------------------------------------------------------
        time.sleep(2)
        if self.log_out_page.get_account__log_out_breadcrumb():
            self.logger.info("Logout Successful")
        # ------------------------------------------------------
        # Click Logout Continue Button
        # ------------------------------------------------------
        time.sleep(2)
        self.log_out_page.click_log_out_continue_button()
        self.logger.info("Clicked On Logout Page")
        # ------------------------------------------------------
        # Verify the homepage title
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        time.sleep(2)
        if self.homepage.get_home_page_title():
            self.logger.info("Navigate to Homepage Successfully")
        self.logger.info("User should be taken to the Home page")
        self.logger.info("========== TC_LG_002 Passed ==========")

    # ==========================================================
    # TC_LG_004
    # Verify logging out and browsing back
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_logout_and_browse_back(self, setup):
        self.logger.info("========== TC_LG_004 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
        self.login_page.enter_password("1234")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("User Logged In Successfully")
        # ------------------------------------------------------
        # Logout
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        time.sleep(3)
        self.homepage.click_logout()
        self.logger.info("Logged Out Successfully")
        # ------------------------------------------------------
        # Browser Back
        # ------------------------------------------------------
        time.sleep(3)
        self.driver.back()
        self.logger.info("Clicked Browser Back Button")

        self.homepage = home_page(self.driver)
        time.sleep(3)
        self.homepage.click_my_account()

        if self.homepage.is_logout_displayed():
            CaptureScrenshot.capture_screenshot(self.driver,"TC_LG_004_Failed")
            pytest.fail("User got logged in again after clicking Browser Back Button")
        self.logger.info("User Remained Logged Out")
        self.logger.info("========== TC_LG_004 Passed ==========")

    # ==========================================================
    # TC_LG_005
    # Verify Logout option is not displayed under
    # 'My Account' menu before logging in
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(5)
    def test_logout_option_not_displayed_before_login(self, setup):
        self.logger.info("========== TC_LG_005 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Verify Logout Is Not Displayed
        # ------------------------------------------------------
        if not self.homepage.is_logout_displayed():
            screenshot_path = (CaptureScrenshot.capture_screenshot(self.driver,
                                                                   " TC_LG_005_Failed"))
            pytest.fail("Logout option is displayed before login")
        self.logger.info("Logout option is not displayed before login")
        self.logger.info("========== TC_LG_005 Passed ==========")

    # ==========================================================
    # TC_LG_006
    # Verify Logout option is not displayed under
    # Right Column options before logging in
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(6)
    def test_logout_not_displayed_in_right_column_before_login(self, setup):
        self.logger.info("========== TC_LG_006 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # ------------------------------------------------------
        # Click Register
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_registration()
        time.sleep(2)
        self.logger.info("Clicked On registration Page")
        # ------------------------------------------------------
        # Verify Logout Not Displayed
        # ------------------------------------------------------
        self.register_page = registerPage(self.driver)
        if not self.register_page.is_logout_display_right_column():
            self.logger.info("Logout option is not displayed in Right Column")
        else:
            pytest.fail("Logout option is displayed in Right Column before login")
        self.logger.info("========== TC_LG_006 Passed ==========")
