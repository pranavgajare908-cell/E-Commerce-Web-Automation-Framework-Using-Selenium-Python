import pytest

from pages import account_success_page
from pages.home_page import home_page
from utilities import screenshot
from utilities.logger import logGen
from utilities.random_email_generator import random_email_generator
from utilities.read_properties import ReadConfig
from pages.registration_page import registerPage
from pages.account_success_page import AccountSuccessPage
from pages.my_account_page import MyAccountPage
from pages.news_letter_page import NewsLetterOption
from utilities.screenshot import CaptureScrenshot


class TestRegister():
    logger = logGen.logger()

    # ==========================================================
    # TC_RF_001
    # Verify Registering an Account by providing only
    # Mandatory fields
    # ==========================================================

    @pytest.mark.regression
    @pytest.mark.order(1)
    def test_register_with_mandatory_fields(self, setup):
        self.logger.info("========== TC_RF_001 Started ==========")
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
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")

        # ------------------------------------------------------
        # Step 4
        # Enter Mandatory Fields
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("pranav")
        self.registration_page.enter_last_name("gajare")

        self.email = random_email_generator.generate_Email()
        self.registration_page.enter_email(self.email)

        self.registration_page.enter_telephone("1234567890")
        self.registration_page.enter_password("1234")
        self.registration_page.enter_confirm_password("1234")
        self.logger.info("Entered All Mandatory Fields")
        self.registration_page.selectNewsLetterOption()

        # ------------------------------------------------------
        # Step 5
        # Select Privacy Policy
        # ------------------------------------------------------
        self.registration_page.selectedPrivacyPolicyField()
        self.logger.info("Privacy Policy Selected")

        # ------------------------------------------------------
        # Step 6
        # Click Continue Button
        # ------------------------------------------------------
        self.registration_page.click_continue_btn()

        self.account_success_page = AccountSuccessPage(self.driver)
        # ------------------------------------------------------
        # Expected Messages
        # ------------------------------------------------------
        properDetailsOne = "Your Account Has Been Created!"
        properDetailsTwo = "Congratulations! Your new account has been successfully created!"
        properDetailsThree = "You can now take advantage of member privileges to enhance your online shopping experience with us."
        properDetailsFour = "If you have ANY questions about the operation of this online shop, please e-mail the store owner."
        properDetailsFive = "A confirmation has been sent to the provided e-mail address. If you have not received it within the hour, please contact us."
        # ------------------------------------------------------
        # Assertions
        # ------------------------------------------------------
        assert properDetailsOne == self.account_success_page.get_success_message_one()
        assert properDetailsTwo == self.account_success_page.get_success_message_two()
        assert properDetailsThree == self.account_success_page.get_success_message_three()
        assert properDetailsFour == self.account_success_page.get_success_message_four()
        assert properDetailsFive == self.account_success_page.get_success_message_five()

        self.logger.info("All Success Messages Validated Successfully")
        # ==========================================================
        # Validate Success Messages
        # ==========================================================

        self.my_account_page = MyAccountPage(self.driver)
        self.logger.info("Clicked On My Account Page Information")
        # ==========================================================
        # Validate is displayed the My Account Page Information
        # ==========================================================
        self.my_account_page = self.account_success_page.click_on_continue_button()
        assert self.my_account_page.did_we_navigate_to_my_account_page()
        self.logger.info("========== TC_RF_001 Passed ==========")

    # ==========================================================
    # TC_RF_004
    # Verify proper notification messages are displayed for the mandatory fields
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_register_without_entering_any_field(self, setup):
        self.logger.info("========== TC_RF_004 Started ==========")
        self.driver = setup
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Step 2
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Click Continue Without Entering Data
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.click_continue_btn()
        self.logger.info("Click Continue Button, Without Entering Any Fields")
        # ======================================================
        # Expected Warning Messages
        # ======================================================
        expected_firstname_warning = ("First Name must be between 1 and 32 characters!")
        expected_lastname_warning = ("Last Name must be between 1 and 32 characters!")
        expected_email_warning = ("E-Mail Address does not appear to be valid!")
        expected_telephone_warning = ("Telephone must be between 3 and 32 characters!")
        expected_password_waring = ("Password must be between 4 and 20 characters!")
        expected_privacy_policy_warning = ("Warning: You must agree to the Privacy Policy!")
        # ======================================================
        # Actual Warning Messages
        # ======================================================
        assert expected_firstname_warning == self.registration_page.get_firstname_warning()
        assert expected_lastname_warning == self.registration_page.get_lastname_warning()
        assert expected_email_warning == self.registration_page.get_email_warning()
        assert expected_telephone_warning == self.registration_page.get_telephone_warning()
        assert expected_password_waring == self.registration_page.get_password_warning()
        assert expected_privacy_policy_warning == self.registration_page.get_privacy_policy_warning()
        self.logger.info("========== TC_RF_004 Passed ==========")

    # ==========================================================
    # TC_RF_005
    # Verify Registering an Account when
    # 'Yes' option is selected for Newsletter
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(3)
    def test_register_account_with_yes_option_for_newsletter(self, setup):
        self.logger.info("========== TC_RF_005 Started ==========")
        self.driver = setup
        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("pranav")
        self.registration_page.enter_last_name("gajare")
        self.email = random_email_generator.generate_Email()
        self.registration_page.enter_email(self.email)
        self.registration_page.enter_telephone("1234567890")
        self.registration_page.enter_password("1234")
        self.registration_page.enter_confirm_password("1234")

        self.logger.info("Entered All Registration Details")
        # ------------------------------------------------------
        # Step 5
        # Select Newsletter Yes Option
        # ------------------------------------------------------
        self.registration_page.selectNewsLetterOption()
        self.logger.info("Selected Yes Option ""For Newsletter")
        # ------------------------------------------------------
        # Step 6
        # Select Privacy Policy
        # ------------------------------------------------------
        self.registration_page.selectedPrivacyPolicyField()
        self.logger.info("Privacy Policy Selected")
        # ------------------------------------------------------
        # Step 7
        # Click Continue Button
        # ------------------------------------------------------
        self.registration_page.click_continue_btn()
        self.logger.info("Clicked Continue Button")
        # ------------------------------------------------------
        # Account Success Page
        # ------------------------------------------------------
        self.account_success_page = AccountSuccessPage(self.driver)
        self.account_success_page.click_on_continue_button()

        self.logger.info("Clicked On Account Success Continue Button")
        # ------------------------------------------------------
        # My Account Page
        # ------------------------------------------------------
        self.my_account_page = MyAccountPage(self.driver)
        self.my_account_page.clickOnSubscribeUnscribeToNewsletterOption()

        self.logger.info("Clicked Continue Button On Account Success Page")

        # ------------------------------------------------------
        # News Letter Page
        # ------------------------------------------------------
        self.newsletter = NewsLetterOption(self.driver)

        assert (self.newsletter.isNewsletterOption())
        self.logger.info("YES Newsletter Option Is Selected")

        self.logger.info("========== TC_RF_005 Passed ==========")

    # ==========================================================
    # TC_RF_006
    # Verify Registering an Account when
    # 'NO' option is selected for Newsletter
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_register_account_with_No_option_for_newsletter(self, setup):
        self.logger.info("========== TC_RF_006 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("pranav")
        self.registration_page.enter_last_name("gajare")
        self.email = random_email_generator.generate_Email()
        self.registration_page.enter_email(self.email)
        self.registration_page.enter_telephone("1234567890")
        self.registration_page.enter_password("1234")
        self.registration_page.enter_confirm_password("1234")

        self.logger.info("Entered All Registration Details")
        # ------------------------------------------------------
        # Step 5
        # Select Newsletter Yes Option
        # ------------------------------------------------------
        # self.registration_page.selectNewsLetterOption()
        # self.logger.info("Selected Yes Option ""For Newsletter")

        # ------------------------------------------------------
        # Step 6
        # Select Privacy Policy
        # ------------------------------------------------------
        self.registration_page.selectedPrivacyPolicyField()
        self.logger.info("Privacy Policy Selected")
        # ------------------------------------------------------
        # Step 7
        # Click Continue Button
        # ------------------------------------------------------
        self.registration_page.click_continue_btn()
        self.logger.info("Clicked Continue Button")
        # ------------------------------------------------------
        # Account Success Page
        # ------------------------------------------------------
        self.account_success_page = AccountSuccessPage(self.driver)
        self.account_success_page.click_on_continue_button()

        self.logger.info("Clicked On Account Success Continue Button")
        # ------------------------------------------------------
        # My Account Page
        # ------------------------------------------------------
        self.my_account_page = MyAccountPage(self.driver)
        self.my_account_page.clickOnSubscribeUnscribeToNewsletterOption()

        self.logger.info("Clicked Continue Button On Account Success Page")

        # ------------------------------------------------------
        # News Letter Page
        # ------------------------------------------------------
        self.newsletter = NewsLetterOption(self.driver)

        assert (self.newsletter.isNewsletterOption_NO())
        self.logger.info("NO Newsletter Option Is Selected")

        self.logger.info("========== TC_RF_006 Passed ==========")

    # ==========================================================
    # TC_RF_008
    # Verify Registering an Account by entering
    # different passwords into Password and
    # Password Confirm fields
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(5)
    def test_register_account_with_different_passwords(self, setup):
        self.logger.info("========== TC_RF_007 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("pranav")
        self.registration_page.enter_last_name("gajare")
        self.email = random_email_generator.generate_Email()
        self.registration_page.enter_email(self.email)
        self.registration_page.enter_telephone("1234567890")
        self.registration_page.enter_password("1234")
        self.registration_page.enter_confirm_password("abcde")
        self.logger.info("Entered Different Confirm Password")

        self.registration_page.selectedPrivacyPolicyField()
        self.logger.info("Privacy Policy Selected")
        # ------------------------------------------------------
        # Step 7
        # Click Continue Button
        # ------------------------------------------------------
        self.registration_page.click_continue_btn()
        self.logger.info("Clicked Continue Button")
        # ======================================================
        # Expected Warning Message
        # ======================================================
        expected_warning_message = ("Password confirmation does not match password!")
        # ======================================================
        # Expected Warning Message
        # ======================================================
        assert (expected_warning_message == self.registration_page.get_password_warning_message())
        self.logger.info("Password Warning Message Validated Successfully")
        self.logger.info("========== TC_RF_008 Passed ==========")

    # ==========================================================
    # TC_RF_009
    # Verify Registering an Account by providing
    # existing account details
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(6)
    def test_register_with_existing_email_address(self, setup):
        self.logger.info("========== TC_RF_009 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("pranav")
        self.registration_page.enter_last_name("gajare")
        self.registration_page.enter_email("pranavgajare908@gmail.com")
        self.registration_page.enter_telephone("1234567890")
        self.registration_page.enter_password("1234")
        self.registration_page.enter_confirm_password("abcde")
        self.logger.info("Entered Different Confirm Password")

        self.registration_page.selectedPrivacyPolicyField()
        self.logger.info("Privacy Policy Selected")
        # ------------------------------------------------------
        # Step 7
        # Click Continue Button
        # ------------------------------------------------------
        self.registration_page.click_continue_btn()
        self.logger.info("Clicked Continue Button")
        # ======================================================
        # Expected Warning Message
        # ======================================================
        expected_warning_message = ("Warning: E-Mail Address is already registered!")
        # ======================================================
        # Expected Warning Message
        # ======================================================
        assert (expected_warning_message == self.registration_page.get_email_already_registered_warning())
        self.logger.info("Existing Email Warning Message Validated Successfully")
        self.logger.info("========== TC_RF_009 Passed ==========")

    # ==========================================================
    # TC_RF_010
    # Verify Registering an Account by providing
    # invalid email addresses
    # ==========================================================
    @pytest.mark.functional
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "Invalid_email",
        [
            "amotoori",
            "amotoori@",
            "amotoori@gmail",
            "amotoori@gmail."
        ]
    )
    @pytest.mark.order(7)
    def test_register_with_invalid_email_address(self, setup, Invalid_email):
        self.logger.info("========== TC_RF_010 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("pranav")
        self.registration_page.enter_last_name("gajare")
        self.registration_page.enter_email(Invalid_email)
        self.registration_page.enter_telephone("1234567890")
        self.registration_page.enter_password("1234")
        self.registration_page.enter_confirm_password("1234")

        self.registration_page.selectedPrivacyPolicyField()
        self.logger.info("Privacy Policy Selected")
        # ------------------------------------------------------
        # Step 7
        # Click Continue Button
        # ------------------------------------------------------
        self.registration_page.click_continue_btn()
        self.logger.info("Clicked Continue Button")
        # ======================================================
        # Browser Validation Message
        # ======================================================
        if Invalid_email in [
            "amotoori",
            "amotoori@",
            "amotoori@gmail."
        ]:
            validation_message = self.registration_page.get_browser_validation_message()
            assert validation_message != ""
            self.logger.info(f"Browser Validation Message: {validation_message}")
        # ======================================================
        # Website Validation Message
        # ======================================================
        elif Invalid_email == "amotoori@gmail":
            expected_message = ("E-Mail Address does not appear to be valid!")
            assert (expected_message == self.registration_page.get_invalid_email_warning_message())
            self.logger.info("========== TC_RF_010 Passed ==========")

    # ==========================================================
    # TC_RF_011
    # Verify Registering an Account by providing
    # invalid phone number
    # ==========================================================
    @pytest.mark.functional
    @pytest.mark.regression
    @pytest.mark.order(8)
    def test_register_with_invalid_phone_number(self, setup):
        self.logger.info("========== TC_RF_011 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("pranav")
        self.registration_page.enter_last_name("gajare")
        self.email = random_email_generator.generate_Email()
        self.registration_page.enter_email(self.email)
        self.registration_page.enter_telephone("asd")
        self.registration_page.enter_password("1234")
        self.registration_page.enter_confirm_password("1234")
        self.registration_page.selectedPrivacyPolicyField()
        self.logger.info("Privacy Policy Selected")
        self.registration_page.click_continue_btn()
        # ------------------------------------------------------
        # Validation
        # ------------------------------------------------------
        try:
            warning_message = (self.registration_page.invalid_telephone_warning_message)
            expected_message = ("Telephone number entered by you is invalid!")
            assert (expected_message == warning_message)
            self.logger.info("Telephone Warning Message Displayed")
        except Exception:
            self.logger.error("BUG FOUND : Account Created With Invalid Phone Number")
            # Screenshot Folder
            # screenshot_path = ("./screenshot/TC_RF_011_Invalid_Phone.png")
            screenshot_path = (
                CaptureScrenshot.capture_screenshot(
                    self.driver, "TC_RF_011_Invalid_Phone"
                )
            )
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot Saved At: {screenshot_path}")
            assert False, ("BUG : Account Created With Invalid Phone Number")

    # ==========================================================
    # TC_RF_012
    # Verify Registering an Account by using
    # Keyboard Keys
    # ==========================================================
    @pytest.mark.functional
    @pytest.mark.regression
    @pytest.mark.order(9)
    def test_register_account_using_keyboard_keys(self, setup):
        self.logger.info("========== TC_RF_012 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Home Page
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Registration Page
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        # First Name
        first_name = self.driver.find_element(By.XPATH, "//input[@id='input-firstname']")
        first_name.send_keys("pranav")
        first_name.send_keys(Keys.TAB)
        # Last Name
        active_element = self.driver.switch_to.active_element
        active_element.send_keys("gajare")
        active_element.send_keys(Keys.TAB)
        # Email
        active_element = self.driver.switch_to.active_element
        self.email = random_email_generator.generate_Email()
        active_element.send_keys(self.email)
        active_element.send_keys(Keys.TAB)
        # telephone
        active_element = self.driver.switch_to.active_element
        active_element.send_keys("1234567890")
        active_element.send_keys(Keys.TAB)
        # Password
        active_element = self.driver.switch_to.active_element
        active_element.send_keys("1234")
        active_element.send_keys(Keys.TAB)
        # Confirm-Password
        active_element = self.driver.switch_to.active_element
        active_element.send_keys("1234")
        active_element.send_keys(Keys.TAB)
        # ------------------------------------------------------
        # Newsletter YES Radio Button
        # ------------------------------------------------------
        active_element = self.driver.switch_to.active_element
        # Select YES Radio Button
        active_element.send_keys(Keys.ARROW_RIGHT)
        active_element.send_keys(Keys.TAB)
        self.logger.info("Selected YES Newsletter Option")
        # ------------------------------------------------------
        # Privacy Policy Checkbox
        # ------------------------------------------------------
        privacy_policy = self.driver.find_element(By.NAME, "agree")
        privacy_policy.send_keys(Keys.SPACE)
        self.logger.info("Selected Privacy Policy Checkbox")
        privacy_policy.send_keys(Keys.TAB)
        # ------------------------------------------------------
        # Continue Button
        # ------------------------------------------------------
        active_element = self.driver.switch_to.active_element
        active_element.send_keys(Keys.ENTER)
        self.logger.info("Registration Form Submitted Using Keyboard Keys")
        # ------------------------------------------------------
        # Account Success Page
        # ------------------------------------------------------
        self.account_success_page = AccountSuccessPage(self.driver)
        assert (self.account_success_page.is_account_successful())
        self.logger.info("User Navigated To Account Success Page")
        assert (self.account_success_page.is_account_successful())
        self.logger.info("Display Logout Button On Account Success Page")

        self.logger.info("========== TC_RF_012 Passed ==========")

    # ==========================================================
    # TC_RF_013
    # Verify all fields have proper placeholders
    # ==========================================================
    @pytest.mark.functional
    @pytest.mark.regression
    @pytest.mark.order(10)
    def test_verify_placeholders_in_register_page(self, setup):
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        # ------------------------------------------------------
        # Expected Placeholders
        # ------------------------------------------------------
        expected_firstname = "First Name"
        expected_lastname = "Last Name"
        expected_email = "E-Mail"
        expected_telephone = "Telephone"
        expected_password = "Password"
        expected_confirm_password = "Password Confirm"
        # ------------------------------------------------------
        # Assertion
        # ------------------------------------------------------
        assert expected_firstname == self.registration_page.get_firstname_placeholder()
        assert expected_lastname == self.registration_page.get_lastname_placeholder()
        assert expected_email == self.registration_page.get_email_placeholder()
        assert expected_telephone == self.registration_page.get_telephone_placeholder()
        assert expected_password == self.registration_page.get_password_placeholder()
        assert expected_confirm_password == self.registration_page.get_confirm_password_placeholder()
        self.logger.info("All Placeholder Values Validated Successfully")
        self.logger.info("========== TC_RF_013 Passed ==========")

    # ==========================================================
    # TC_RF_014
    # Verify mandatory fields are marked
    # with red color * symbol
    # ==========================================================
    @pytest.mark.functional
    @pytest.mark.regression
    @pytest.mark.order(11)
    def test_verify_mandatory_fields_marked_with_red_asterisk(self, setup):
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        # ------------------------------------------------------
        # Assertion
        # ------------------------------------------------------
        assert "col-sm-2 control-label" == self.registration_page.get_first_name_label()
        assert "col-sm-2 control-label" == self.registration_page.get_last_name_label()
        assert "col-sm-2 control-label" == self.registration_page.get_email_label()
        assert "col-sm-2 control-label" == self.registration_page.get_telephone_label()
        assert "col-sm-2 control-label" == self.registration_page.get_password_label()
        assert "col-sm-2 control-label" == self.registration_page.get_confirm_password_label()
        self.logger.info("All Mandatory Fields Are Marked With Red asterisk")
        self.logger.info("========== TC_RF_014 Passed ==========")

    # ==========================================================
    # TC_RF_016
    # Verify Mandatory Fields Are Not Accepting Only Spaces
    # ==========================================================
    @pytest.mark.functional
    @pytest.mark.regression
    @pytest.mark.order(12)
    def test_register_with_spaces_in_mandatory_fields(self, setup):
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("        ")
        self.registration_page.enter_last_name("        ")
        self.registration_page.enter_email("        ")
        self.registration_page.enter_telephone("        ")
        self.registration_page.enter_password("        ")
        self.registration_page.enter_confirm_password("            ")
        # ------------------------------------------------------
        # Privacy Policy
        self.registration_page.selectedPrivacyPolicyField()
        # ------------------------------------------------------

        # ------------------------------------------------------
        # continue button
        self.registration_page.click_continue_btn()
        self.logger.info("Clicked Continue Button")
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Expected Warning Message
        # ------------------------------------------------------
        expected_firstname_warning = "First Name must be between 1 and 32 characters!"
        expected_lastname_warning = "Last Name must be between 1 and 32 characters!"
        expected_email_warning = "E-Mail Address does not appear to be valid!"
        # ------------------------------------------------------
        # Assertion
        # ------------------------------------------------------
        assert (expected_firstname_warning == self.registration_page.get_firstname_warning())
        assert (expected_lastname_warning == self.registration_page.get_lastname_warning())
        assert (expected_email_warning == self.registration_page.get_email_warning())

        try:
            expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
            warning_telephone_message = self.registration_page.get_telephone_warning()
            assert (warning_telephone_message == expected_telephone_warning)
            self.logger.info("Telephone Warning Message Are Displayed")
        except Exception as e:
            self.logger.error(f"BUG: Telephone Warning Message Are is not displayed. {str(e)}")
            # ------------------------------------------------------
            # screenshot folder
            # screenshot_path = ("./screenshot/TC_RF_016_Invalid_Phone.png")
            # ------------------------------------------------------
            screenshot_path = (
                CaptureScrenshot.capture_screenshot(self.driver,
                                                    "TC_RF_016_Telephone_Warning_Not_Displayed.png")
            )
            pytest.fail("Application Bug: Telephone field accepted spaces without displaying warning message.")
        self.logger.info("========== TC_RF_016 Passed ==========")

    # ==========================================================
    # TC_RF_017
    # Verify whether the Password fields
    #  in the Register Account page are following Password Complexity Standards
    # ==========================================================

    @pytest.mark.functional
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "password",
        [
            "12345",
            "abcdefghi",
            "abcd1234",
            "abcd123$",
            "ABCD456#"
        ]
    )
    @pytest.mark.order(13)
    def test_password_complexity_standards(self, setup, password):
        self.logger.info(f"========== TC_RF_017 Started : {password} ==========")

        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        self.logger.info("Application Opened Successfully")
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account Page")
        # ------------------------------------------------------
        # Step 3
        # Click Register
        # ------------------------------------------------------
        self.homepage.click_registration()
        self.logger.info("Clicked On Registration Page")
        # ------------------------------------------------------
        # Step 4
        # Enter Registration Details
        # ------------------------------------------------------
        self.registration_page = registerPage(self.driver)
        self.registration_page.enter_first_name("pranav")
        self.registration_page.enter_last_name("gajare")
        email = random_email_generator.generate_Email()
        self.registration_page.enter_email(email)
        self.registration_page.enter_telephone("1234567890")
        self.registration_page.enter_password(password)
        self.registration_page.enter_confirm_password(password)
        # ------------------------------------------------------
        # Click Privacy Polocy
        # ------------------------------------------------------
        self.registration_page.selectedPrivacyPolicyField()
        # ------------------------------------------------------
        # Click Continue Button
        # ------------------------------------------------------
        self.registration_page.click_continue_btn()
        self.logger.info(f"Enter Pasword: {password}")
        # ------------------------------------------------------
        # Verify Complexity Validation
        # ------------------------------------------------------
        try:
            warning_message = (self.registration_page.get_password_warning())
            expected_message = ("Password must be between 4 and 20 characters!")
            # ------------------------------------------------------
            # Assert
            # ------------------------------------------------------
            assert (warning_message == expected_message)
            self.logger.info( f"Password Warning Displayed :{warning_message}")

        except Exception:
            self.logger.error(f"BUG: Weak password accepted : {password}")
            # ------------------------------------------------------
            # ScreenShot
            # ------------------------------------------------------
            CaptureScrenshot.capture_screenshot(self.driver, f"TC_RF_017_{password}.png")
            pytest.fail(f"Password '{password}' accepted without complexity validation.")
        self.logger.info("========== TC_RF_017 Passed ==========")
