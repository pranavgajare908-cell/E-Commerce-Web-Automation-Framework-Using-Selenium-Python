import time

import pyperclip
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v146.page import capture_screenshot
from selenium.webdriver.support.wait import WebDriverWait as EC, WebDriverWait

from pages.login_page import loginPage
from pages.home_page import home_page
from pages.my_account_page import MyAccountPage
from utilities.logger import logGen
from utilities.read_properties import ReadConfig
from utilities.screenshot import CaptureScrenshot
from pages.forgot_password_page import forgot_password_Page
from pages.home_page import home_page as HomePage
from pages.change_password_page import MyAccount_ChangePasswordPage


class TestLogin:
    logger = logGen.logger()

    # ==========================================================
    # TC_LF_001
    # Verify logging into the Application
    # using valid credentials
    # ==========================================================
    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_login_with_valid_credentials(self, setup):
        self.logger.info("========== TC_LF_001 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # Enter Valid Credential
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
        self.login_page.enter_password("1234")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("Clicked On Login Buttom")
        # ------------------------------------------------------
        # Navigate to the MyAccount Page
        # ------------------------------------------------------
        self.my_account = MyAccountPage(self.driver)
        # ------------------------------------------------------
        # Assertion to check logout linktext is displayed
        # ------------------------------------------------------
        assert (self.my_account.did_we_navigate_logout_to_my_account_page())
        self.logger.info("User Successfully Logged In")
        self.logger.info("========== TC_LF_001 Passed ==========")

    # ==========================================================
    # TC_LF_002
    # Verify logging into the Application using invalid
    # credentials
    # ==========================================================
    @pytest.mark.functional
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "email,password",
        [
            ("xyzabc123@gmail.com", "xyzabc123"),
            # ("pranavgajare908@gmail.com", "12345"),
            ("amotoori3@gmail.com", "xyzabc123")
        ]
    )
    @pytest.mark.order(2)
    def test_login_with_invalid_credentials(self, setup, email, password):
        self.logger.info("========== TC_LF_002 and TC_LF_003 and TC_LF_004 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Invalid Credential
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address(email)
        self.login_page.enter_password(password)
        self.logger.info(f"Enter Email: {email} and Password: {password}")
        # ------------------------------------------------------
        # Click on Login Page
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("Clicked On Login Buttom")

        try:
            expect_warning_message = "Warning: No match for E-Mail Address and/or Password."
            # ------------------------------------------------------
            # Assertion
            # ------------------------------------------------------
            assert (expect_warning_message == self.login_page.get_login_warning_message())
            self.logger.info(f"{expect_warning_message} Successfully Validate")
        except Exception as e:
            self.logger.error(f"BUG FOUND : Login Invalid Credentials {str(e)}")
            # ------------------------------------------------------
            # Capture Screenshot
            # ------------------------------------------------------
            screenshot_path = (
                CaptureScrenshot.capture_screenshot(self.driver,
                                                    "TC_LF_002_Invalid_Credential")
            )
            pytest.fail("Applicaion Bug: Warning message not displayed")
        self.logger.info("========== TC_LF_002 Passed ==========")

    # ==========================================================
    # TC_LF_005
    # Verify logging into the Application
    # without providing any credentials
    # ==========================================================
    @pytest.mark.sanity
    @pytest.mark.order(3)
    def test_login_without_credentials(self, setup):
        self.logger.info("========== TC_LF_005 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # Leave Email and Password Blank
        # Click Login
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("")
        self.login_page.enter_password("")
        # ------------------------------------------------------
        # Click Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("Clicked On Login Buttom")
        expected_warning = "Warning: No match for E-Mail Address and/or Password."
        # ------------------------------------------------------
        # Assertion
        # ------------------------------------------------------
        assert (expected_warning == self.login_page.get_login_warning_message())
        self.logger.info(f"{expected_warning} Displayed Successfully")
        self.logger.info("========== TC_LF_005 Passed ==========")

    # ==========================================================
    # TC_LF_006
    # Verify 'Forgotten Password' link is
    # available in the Login page and is working
    # ==========================================================
    @pytest.mark.sanity
    @pytest.mark.order(4)
    def test_forgotten_password_link(self, setup):
        self.logger.info("========== TC_LF_006 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        self.login_page = loginPage(self.driver)
        # ------------------------------------------------------
        # Step 4
        # Click Forgot Password
        # ------------------------------------------------------
        self.login_page.click_forgotten_password()
        # ------------------------------------------------------
        # Step 5
        # Validate the Navigate to the Forgot Password Page
        # ------------------------------------------------------
        self.forgot_password = forgot_password_Page(self.driver)
        self.forgot_password.did_we_navigate_to_forgotten_password_page()
        self.logger.info("Forgotten Password Page Displayed Successfully")
        self.logger.info("========== TC_LF_006 Passed ==========")

    # ==========================================================
    # TC_LF_007
    # Verify logging into the Application
    # using Keyboard keys (Tab and Enter)
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(5)
    def test_login_using_keyboard_keys(self, setup):
        self.logger.info("========== TC_LF_007 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")

        self.login_page = loginPage(self.driver)
        # ------------------------------------------------------
        # Login Using Keyboard Keys
        # ------------------------------------------------------
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        # ------------------------------------------------------
        # email_field
        # ------------------------------------------------------
        email_field = self.driver.find_element(By.XPATH, "//input[@id='input-email']")
        email_field.send_keys("pranavgajare908@gmail.com")
        email_field.send_keys(Keys.TAB)
        # ------------------------------------------------------
        # password field
        # ------------------------------------------------------
        active_element = self.driver.switch_to.active_element
        active_element.send_keys("1234")
        active_element.send_keys(Keys.TAB)
        # ------------------------------------------------------
        # move to forgotten password
        active_element.send_keys(Keys.TAB)
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Get the new focused element
        active_element = self.driver.switch_to.active_element
        # ------------------------------------------------------

        # ------------------------------------------------------
        # TAB -> Login Button
        active_element.send_keys(Keys.TAB)
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Get the new focused element
        active_element = self.driver.switch_to.active_element
        # ------------------------------------------------------

        # ------------------------------------------------------
        # ENTER on Login Button
        # ------------------------------------------------------
        active_element.send_keys(Keys.ENTER)

        self.logger.info("Login Form Submitted Using Keyboard")
        # ------------------------------------------------------
        # Validate Login Success
        # ------------------------------------------------------
        self.my_account = MyAccountPage(self.driver)
        # ------------------------------------------------------
        # did we navigate to my account page
        # ------------------------------------------------------
        self.my_account.did_we_navigate_to_my_account_page()
        self.logger.info("User Logged In Successfully")
        self.logger.info("========== TC_LF_007 Passed ==========")

    # ==========================================================
    # TC_LF_008
    # Verify E-Mail Address and Password text fields
    # in the Login page have the place holder text
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(6)
    def test_verify_login_placeholders(self, setup):
        self.logger.info("========== TC_LF_008 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        self.login_page = loginPage(self.driver)
        # ------------------------------------------------------
        # Expected Placeholders
        # ------------------------------------------------------
        expected_email_field_placeholder = "E-Mail Address"
        expected_password_field_placeholder = ("Password")
        # ------------------------------------------------------
        # Assertion
        # ------------------------------------------------------
        assert (expected_email_field_placeholder == self.login_page.get_email_field_placeholder())
        assert (expected_password_field_placeholder == self.login_page.get_password_field_placeholder())
        self.logger.info(
            f"Email Field Placeholder {expected_email_field_placeholder} and Password Field Placeholder {expected_password_field_placeholder} Are Displayed Successfully")
        self.logger.info("========== TC_LF_008 Passed ==========")

    # ==========================================================
    # TC_LF_009
    # Verify Logging into the Application and
    # browsing back using Browser Back button
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(7)
    def test_login_and_browser_back_button(self, setup):
        self.logger.info("========== TC_LF_009 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")

        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
        self.login_page.enter_password("1234")
        # ------------------------------------------------------
        # Step 4
        # Click Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("User Logged In Successfully")
        # ------------------------------------------------------
        # My Account
        # ------------------------------------------------------
        self.my_account = MyAccountPage(self.driver)
        assert (self.my_account.did_we_navigate_logout_to_my_account_page())
        time.sleep(5)
        self.logger.info("User Successfully Logged In")
        self.driver.back()
        self.logger.info("Clicked Browser Back Button")
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        try:

            # ------------------------------------------------------
            # Assert to display logout button when user should loged in
            # ------------------------------------------------------
            assert (self.homepage.is_logout_displayed())
            self.logger.info("User is still logged in after clicking Browser Back Button")

        except AssertionError:
            self.logger.error("BUG: User Logged Out After Clicking Browser Back Button")

            screenshot_path = (
                CaptureScrenshot.capture_screenshot(self.driver,
                                                    "TC_LF_009_BackButton_UserLoggedOut")
            )
            self.logger.info(f"Screenshot Saved At: {screenshot_path}")
            pytest.fail("TC_LF_009 Failed: User session was not maintained after clicking the browser Back button.")
        self.logger.info("========== TC_LF_009 Passed ==========")

    # ==========================================================
    # TC_LF_010
    # Verify Logging out from the Application and
    # browsing back using Browser Back button
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(8)
    def test_logout_and_browser_back_button(self, setup):
        self.logger.info("========== TC_LF_010 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # Enter Valid Credential
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
        self.login_page.enter_password("1234")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("Clicked On Login Buttom")
        self.logger.info("Loged In Successfully")
        # ------------------------------------------------------
        # Click on Logout Button
        # ------------------------------------------------------
        time.sleep(5)
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.homepage.click_logout()
        self.logger.info("Clicked On Logout Page")
        # ------------------------------------------------------
        # Validate Logout Page
        # ------------------------------------------------------
        assert "logout" in self.driver.current_url.lower()
        time.sleep(5)
        self.driver.back()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script(
                "return document.readyState") == "complete")

        self.logger.info("Clicked Browser Back Button")
        # ------------------------------------------------------
        # Verify User Is Not Logged In Again
        # ------------------------------------------------------

        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        if self.homepage.is_logout_displayed():
            self.logger.error("BUG: User got logged in again after clicking Browser Back Button")

            screen_shot_path = (CaptureScrenshot.capture_screenshot(self.driver,
                                                                    "TC_LF_010_User_Logged_In_Again"))
            pytest.fail("TC_LF_010 Failed: User got logged in again after clicking Browser Back Button.")
        self.logger.info("========== TC_LF_010 Passed ==========")

    # ==========================================================
    # TC_LF_011
    # Verify logging into the Application using
    # inactive credentials
    # ==========================================================
    @pytest.mark.sanity
    @pytest.mark.order(9)
    def test_login_with_inactive_credentials(self, setup):
        self.logger.info("========== TC_LF_011 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # Enter Valid Credential
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("amotooricap123454321@gmail.com")
        self.login_page.enter_password("12345")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("Clicked On Login Buttom")
        # ------------------------------------------------------
        # Validate Warning Message
        # ------------------------------------------------------
        expected_warning = ("Warning: No match for E-Mail Address and/or Password.")
        try:
            actual_warning = (self.login_page.get_login_warning_message())
            assert expected_warning == actual_warning
            self.logger.info("Warning Message Validated Successfully")
        except Exception as e:
            self.logger.error(f"BUG FOUND: {str(e)}")
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_LF_011_Inactive_Credentials")
            pytest.fail("TC_LF_011 Failed: Inactive account was allowed to login.")
        self.logger.info("========== TC_LF_011 Passed ==========")

    # ==========================================================
    # TC_LF_013
    # Verify the text entered into the Password field
    # is toggled to hide its visibility
    # ==========================================================
    @pytest.mark.sanity
    @pytest.mark.order(10)
    def test_password_field_is_masked(self, setup):
        self.logger.info("========== TC_LF_013 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # Enter Password
        # ------------------------------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.enter_password("12345")
        self.logger.info("Entered Password")
        # ------------------------------------------------------
        # Verify Password Field Type
        # ------------------------------------------------------
        assert self.login_page.get_password_field_type() == "password"
        self.logger.info("Password Field Is Masked Successfully")
        self.logger.info("========== TC_LF_013 Passed ==========")

    # ==========================================================
    # TC_LF_014
    # Verify the copying of the text entered into the
    # Password field
    # ==========================================================
    import pyperclip
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    @pytest.mark.regression
    @pytest.mark.order(11)
    def test_copy_password_field(self, setup):
        self.logger.info("========== TC_LF_014 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Step 3
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        self.login_page = loginPage(self.driver)
        password_field = self.driver.find_element(By.XPATH, "//input[@id='input-password']")
        password_text = "Test12345"
        password_field.send_keys(password_text)
        # ------------------------------------------------------
        # Select All
        # ------------------------------------------------------
        password_field.send_keys(Keys.CONTROL, "a")
        # ------------------------------------------------------
        # Copy
        # ------------------------------------------------------
        password_field.send_keys(Keys.CONTROL, "c")
        clipboard_text = pyperclip.paste()
        if clipboard_text == password_text:
            pytest.fail("BUG: Password text was copied successfully.")
        self.logger.info("Password text was not copied.")

        self.logger.info("========== TC_LF_014 Passed ==========")

    # ==========================================================
    # TC_LF_016
    # Verify Logging into the Application
    # after changing the password
    # ==========================================================
    # @pytest.mark.sanity
    # @pytest.mark.order(12)
    # def test_login_after_changing_password(self, setup):
    #     self.logger.info("========== TC_LF_016 Started ==========")
    #     self.driver = setup
    #     self.driver.get(
    #         ReadConfig.get_application_URL()
    #     )
    #     # ------------------------------------------------------
    #     # Step 1
    #     # Open Application
    #     # ------------------------------------------------------
    #     self.logger.info("Application Opened Successfully")
    #     # ------------------------------------------------------
    #     # Step 2
    #     # Click My Account
    #     # ------------------------------------------------------
    #     self.homepage = home_page(self.driver)
    #     self.homepage.click_my_account()
    #     self.logger.info("Clicked On My Account")
    #     # ------------------------------------------------------
    #     # Step 3
    #     # Click Login
    #     # ------------------------------------------------------
    #     self.homepage.click_login()
    #     self.logger.info("Clicked On Login Page")
    #     # ------------------------------------------------------
    #     # Enter Valid Credential
    #     # ------------------------------------------------------
    #     self.login_page = loginPage(self.driver)
    #     self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
    #     self.login_page.enter_password("1234")
    #     # ------------------------------------------------------
    #     # Click on Login Button
    #     # ------------------------------------------------------
    #     self.login_page.click_login_button()
    #     self.logger.info("Clicked On Login Buttom")
    #     # ------------------------------------------------------
    #     # Navigate to the MyAccount Page
    #     # ------------------------------------------------------
    #     self.my_account = MyAccountPage(self.driver)
    #     time.sleep(5)
    #     self.my_account.click_on_change_password()
    #     self.logger.info("Clicked Change Password Link")
    #     # ------------------------------------------------------
    #     # Navigate to the Change Password
    #     # ------------------------------------------------------
    #     self.MyAccount_change_password = MyAccount_ChangePasswordPage(self.driver)
    #     time.sleep(3)
    #     self.MyAccount_change_password.enter_change_password("12345")
    #     self.MyAccount_change_password.enter_confirm_password("12345")
    #     # ------------------------------------------------------
    #     # Clicked on Chnage Password Continue Password Button
    #     # ------------------------------------------------------
    #     self.MyAccount_change_password.click_continue_button()
    #     self.logger.info("Clicked On Login Page")
    #     # ------------------------------------------------------
    #     # Validation Change Password Success Message
    #     # ------------------------------------------------------
    #     actual_success_change_password = "Success: Your password has been successfully updated."
    #     time.sleep(2)
    #     assert (
    #             actual_success_change_password == self.MyAccount_change_password.get_alert_change_password_success_message())
    #     self.logger.info("Change Message Validated Successfully")
    #     # ------------------------------------------------------
    #     # Logout
    #     # ------------------------------------------------------
    #     time.sleep(3)
    #     self.homepage = home_page(self.driver)
    #     self.homepage.click_my_account()
    #     time.sleep(2)
    #     self.homepage.click_logout()
    #     self.logger.info("Logged Out Successfully")
    #     # ------------------------------------------------------
    #     # Try Login Using Old Password
    #     # ------------------------------------------------------
    #     self.homepage = home_page(self.driver)
    #     time.sleep(2)
    #     self.homepage.click_my_account()
    #     time.sleep(2)
    #     self.homepage.click_login()
    #     self.logger.info("Clicked On Login Page")
    #     self.login_page = loginPage(self.driver)
    #     self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
    #     self.login_page.enter_password("1234")
    #     self.login_page.click_login_button()
    #     expected_warning = "Warning: No match for E-Mail Address and/or Password."
    #     time.sleep(2)
    #     assert (expected_warning == self.login_page.get_login_warning_message())
    #     self.logger.info("Old Password Login Failed As Expected")
    #     # ------------------------------------------------------
    #     # Login Using New Password
    #     # ------------------------------------------------------
    #     self.login_page = loginPage(self.driver)
    #     time.sleep(2)
    #     self.login_page.get_clear_password_field_type()
    #     self.login_page.enter_password("12345")
    #     self.login_page.click_login_button()
    #     self.logger.info("Logged in Successfully With New Password")
    #     # ------------------------------------------------------
    #     # Validate Login Success
    #     # ------------------------------------------------------
    #     self.my_account = MyAccountPage(self.driver)
    #     time.sleep(2)
    #     if self.my_account.did_we_navigate_on_verify_account_breadcrumb():
    #         self.logger.info("Successfully Logged In Using New Password")
    #     self.logger.info("========== TC_LF_016 Passed ==========")

    # ==========================================================
    # TC_LF_019
    # Verify user is able to navigate to different pages
    # from Login page
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(14)
    def test_navigation_from_login_page(self, setup):
        self.logger.info("========== TC_LF_019 Started ==========")
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
        self.homepage.click_login()
        self.logger.info("Navigated To Login Page")
        # ------------------------------------------------------
        # Continue Button -> Register Page
        # -----------------------------------
        self.login_page = loginPage(self.driver)
        self.login_page.click_on_new_customer_continue_button()
        assert "register" in self.driver.current_url.lower()
        self.logger.info("User Navigated To Register Account Page Successfully")
        # -----------------------------------
        # Navigate Back To Login Page
        # -----------------------------------
        self.driver.back()
        # -----------------------------------
        # Navigate Register Page
        # -----------------------------------
        self.login_page.click_right_side_bar_register_page_link()
        assert "register" in self.driver.current_url.lower()
        self.logger.info("User Navigated To Register Account Page Successfully")
        # -----------------------------------
        # Navigate Back To Login Page
        # -----------------------------------
        self.driver.back()
        self.logger.info("========== TC_LF_019 Passed ==========")








