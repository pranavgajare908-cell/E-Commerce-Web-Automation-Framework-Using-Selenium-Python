import time

import pytest
from selenium.webdriver.support.select import Select

from pages import search_page
from utilities.logger import logGen
from utilities.read_properties import ReadConfig
from pages.home_page import home_page
from pages.search_page import SearchPage
from utilities.screenshot import CaptureScrenshot
from pages.login_page import loginPage
from pages.product_compare_page import ProductComparePage


class TestSearch:
    logger = logGen.logger()

    # ==========================================================
    # TC_SF_001
    # Verify searching with an existing Product Name
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(1)
    def test_search_with_existing_product(self, setup):
        self.logger.info("========== TC_SF_001 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        # Search Product
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.enter_product_name("iMac")
        self.logger.info("Entered Product Name : iMac")
        time.sleep(2)
        self.homepage.click_search_product()
        self.logger.info("Clicked Search Button")
        # ------------------------------------------------------
        # Navigate to Search Page & Verify Product Displayed
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        try:
            actual_product_info = "Just when you thought iMac had everything, now there´s even more. More powerful Intel Core 2 Duo pro.."
            assert (actual_product_info == self.searchpage.get_product_info())
            self.logger.info(f"{actual_product_info}")
        except AssertionError:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_001_Failed")
            pytest.fail("iMac Product Not Displayed")
        self.logger.info("========== TC_SF_001 Passed ==========")

    # ==========================================================
    # TC_SF_002
    # Verify searching with a non-existing Product Name
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_search_with_non_existing_product(self, setup):
        self.logger.info("========== TC_SF_002 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.enter_product_name("Fitbit")
        self.logger.info("Entered Product Name : Fitbit")
        time.sleep(2)
        self.homepage.click_search_product()
        # ------------------------------------------------------
        # Verify Warning Message
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        expected_message = "There is no product that matches the search criteria."
        actual_message = self.searchpage.get_warning_product_message()
        if expected_message == actual_message:
            self.logger.info("Proper No Product Message Displayed")
            assert True
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_002_Failed")
            pytest.fail(f"Expected: {expected_message}, "f"Actual: {actual_message}")

        self.logger.info("========== TC_SF_002 Passed ==========")

    # ==========================================================
    # TC_SF_003
    # Verify searching without providing any Product Name
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(3)
    def test_search_without_product_name(self, setup):
        self.logger.info("========== TC_SF_003 Started ==========")
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
        self.homepage = home_page(self.driver)
        time.sleep(2)
        self.homepage.click_search_product()
        self.logger.info("Clicked Search Button Without Product Name")
        # ------------------------------------------------------
        # Verify Warning Message
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        try:
            expected_message = "There is no product that matches the search criteria."
            assert (expected_message == self.searchpage.get_warning_product_message())
            self.logger.info(f"{expected_message} Displayed ")
        except AssertionError:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_003_Failed")
            pytest.fail("Warning Message not displayed")

        self.logger.info("========== TC_SF_003 Passed ==========")

    # ==========================================================
    # TC_SF_004
    # Verify searching for a product after login
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_search_product_after_login(self, setup):
        self.logger.info("========== TC_SF_004 Started ==========")
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
        self.login_page = loginPage(self.driver)
        self.login_page.enter_e_mail_address("pranavgajare908@gmail.com")
        self.login_page.enter_password("1234")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.login_page.click_login_button()
        self.logger.info("User Logged In Successfully")
        # ------------------------------------------------------
        # Search Existing Product
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.enter_product_name("iMac")
        self.logger.info("Entered Product Name : iMac")
        time.sleep(2)
        self.homepage.click_search_product()
        self.logger.info("Clicked Search Button")
        # ------------------------------------------------------
        # Verify Search Result
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        if self.searchpage.did_navigate_to_product_page():
            self.logger.info("Proper No Product Message Displayed")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_004_Failed")
            pytest.fail("Product did not displayed")

        self.logger.info("========== TC_SF_004 Passed ==========")

    # ==========================================================
    # TC_SF_005
    # Verify searching with search criteria resulting
    # in multiple products
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(5)
    def test_search_with_multiple_products(self, setup):
        self.logger.info("========== TC_SF_005 Started ==========")
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
        self.homepage = home_page(self.driver)
        self.homepage.enter_product_name("iMac")
        self.logger.info("Entered Search Criteria : Mac")
        time.sleep(2)
        self.homepage.click_search_product()
        self.logger.info("Clicked Search Button")
        # ------------------------------------------------------
        # Verify Multiple Products Displayed
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        product_count = self.searchpage.get_search_result_count()
        if product_count > 1:
            self.logger.info(f"Multiple Products Displayed : {product_count}")
        else:
            CaptureScrenshot.capture_screenshot(
                self.driver,
                "TC_SF_005_Failed"
            )
            pytest.fail(f"Expected Multiple Products, Found {product_count}")

        self.logger.info("========== TC_SF_005 Passed ==========")

    # ==========================================================
    # TC_SF_006
    # Verify all Search fields have placeholders
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(6)
    def test_verify_search_placeholders(self, setup):
        self.logger.info("========== TC_SF_006 Started ==========")
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
        # Verify Home Page Search Placeholder
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        home_placeholder = self.homepage.get_search_placeholder()
        if home_placeholder == "Search":
            self.logger.info("Home Page Search Placeholder Verified")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_006_Home_Search_Placeholder_Failed")
            pytest.fail(f"Expected Search, Actual {home_placeholder}")

        # ------------------------------------------------------
        # Navigate To Search Page
        # ------------------------------------------------------
        self.homepage.click_search_product()
        # ------------------------------------------------------
        # Verify Search Criteria Placeholder
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        criteria_placeholder = self.searchpage.get_keyword_criteria_placeholder()
        if criteria_placeholder == "Keywords":
            self.logger.info("Search Criteria Placeholder Verified")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_006_Home_Criteria_Placeholder_Failed")
            pytest.fail(f"Expected Keywords, Actual {criteria_placeholder}")

        self.logger.info("========== TC_SF_006 Passed ==========")

    # ==========================================================
    # TC_SF_007
    # Verify searching using Search Criteria field
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(7)
    def test_search_using_search_criteria_field(self, setup):
        self.logger.info("========== TC_SF_007 Started ==========")
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
        # Click Search Icon Without Entering Product
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_search_product()
        self.logger.info("Clicked Search Icon")
        # ------------------------------------------------------
        # Enter Product Name In Search Criteria
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        self.searchpage.enter_search_product_criteria("iMac")
        self.logger.info("Entered Product Name : iMac")
        self.searchpage.click_search_button()
        self.logger.info("Clicked Search Button")
        # ------------------------------------------------------
        # Verify Product Displayed
        # ------------------------------------------------------
        if self.searchpage.did_navigate_to_product_page():
            self.logger.info("iMac Product Displayed Successfully")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_007_Failed")
            pytest.fail("iMac Product Not Displayed")

        self.logger.info("========== TC_SF_007 Passed ==========")

    # ==========================================================
    # TC_SF_008
    # Verify Search using Product Description Text
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(8)
    def test_search_using_product_description(self, setup):
        self.logger.info("========== TC_SF_008 Started ==========")
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
        # ------------------------------------------------------
        # Click Search Icon Without Entering Product
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_search_product()
        self.logger.info("Clicked Search Icon")
        # ------------------------------------------------------
        # Enter Product Name In Search Criteria
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        self.searchpage.enter_search_product_criteria("iLife")
        self.logger.info("Entered Search Criteria : iLife")
        # ------------------------------------------------------
        # Select Search In Product Description
        # ------------------------------------------------------
        self.searchpage.click_check_search_product_description()
        self.logger.info("Selected Search In Product Description")
        # ------------------------------------------------------
        # Click Search Button
        # ------------------------------------------------------
        self.searchpage.click_search_button()
        # ------------------------------------------------------
        # Verify iMac Displayed
        # ------------------------------------------------------
        if self.searchpage.did_navigate_to_product_page():
            self.logger.info("iMac Product Displayed Successfully")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_008_Failed")
            pytest.fail("iMac Product Not Displayed")
        self.logger.info("========== TC_SF_008 Passed ==========")

    # ==========================================================
    # TC_SF_009
    # Verify Search By Selecting Product Category
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(9)
    def test_search_using_product_category(self, setup):
        self.logger.info("========== TC_SF_009 Started ==========")
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
        # Open Search Page
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_search_product()
        self.logger.info("Navigated To Search Page")
        self.searchpage = SearchPage(self.driver)
        # ------------------------------------------------------
        # ER-1
        # Search Using Correct Category
        # ------------------------------------------------------
        self.searchpage.enter_search_product_criteria("iMac")
        # self.searchpage.print_categories()
        self.searchpage.select_drp_category("Mac")
        time.sleep(2)
        self.searchpage.click_search_button()
        if self.searchpage.did_navigate_to_product_page():
            self.logger.info("iMac Displayed With Correct Category")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_009_ER1_Failed")
            pytest.fail("iMac Not Displayed For Correct Category")

        # ------------------------------------------------------
        # ER-2
        # Search Using Wrong Category
        # ------------------------------------------------------
        self.searchpage.enter_search_product_criteria("iMac")
        self.searchpage.select_drp_category("PC")
        time.sleep(2)
        self.searchpage.click_search_button()
        if self.searchpage.is_no_product_warning_message():
            self.logger.info("No Product Message Displayed For Wrong Category")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_009_ER2_Failed")
            pytest.fail("No Product Message Not Displayed For Wrong Category")

        self.logger.info("========== TC_SF_009 Passed ==========")

    # ==========================================================
    # TC_SF_010
    # Verify Search By Selecting Search In Subcategories
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(10)
    def test_search_in_subcategories(self, setup):
        self.logger.info("========== TC_SF_010 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_search_product()
        self.logger.info("Navigated To Search Page")
        self.searchpage = SearchPage(self.driver)
        # ------------------------------------------------------
        # ER-1
        # Search Without Selecting Subcategories
        # ------------------------------------------------------
        self.searchpage.enter_search_product_criteria("iMac")
        categories = self.searchpage.select_drp_category()
        category_found = False
        for category in categories:
            if category.text.strip() == "Desktops":
                category.click()
                category_found = True
                break
        time.sleep(2)
        self.searchpage.click_search_button()
        if self.searchpage.get_warning_product_message():
            self.logger.info("No Product Message Displayed Successfully")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_SF_010_ER1_Failed")

            pytest.fail("Product Displayed Without Selecting Subcategories")

        # # ------------------------------------------------------
        # # ER-2
        # # Search By Selecting Subcategories
        # # ------------------------------------------------------
        # self.searchpage.enter_search_product_criteria("iMac")
        # categories = self.searchpage.select_drp_category()
        # category_found = False
        # for category in categories:
        #     if category.text.strip() == "Desktops":
        #         category.click()
        #         category_found = True
        #         break
        #
        # self.searchpage.click_subcategory_chkbox()
        # time.sleep(3)
        # self.searchpage.click_search_button()
        # if self.searchpage.did_navigate_to_product_page():
        #     self.logger.info("iMac Product Displayed Successfully")
        # else:
        #     CaptureScrenshot.capture_screenshot(self.driver,
        #                                         "TC_SF_010_ER2_Failed")
        #     pytest.fail("iMac Not Displayed After Selecting Subcategories")
        #
        # self.logger.info("========== TC_SF_010 Passed ==========")

    # ==========================================================
    # TC_SF_011
    # Verify List and Grid views when only
    # one Product is displayed in the search results
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(11)
    def test_list_and_grid_view_single_product(self, setup):
        self.logger.info("========== TC_SF_011 Started ==========")
        self.logger.info("========== TC_LF_017 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        # ------------------------------------------------------
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.enter_product_name("iMac")
        self.homepage.click_search_product()
        self.logger.info("Searched Product : iMac")
        # -----------------------------------
        # LIST VIEW
        # -----------------------------------
        self.searchpage = SearchPage(self.driver)
        self.searchpage.click_list_view()
        self.logger.info("Clicked List View")
        if self.searchpage.is_display_product_image():
            self.logger.info("Product Image Displayed In List View")
        else:
            pytest.fail("Product Not Displayed In List View")
        self.searchpage.click_product_image()
        self.logger.info("Clicked Product Name")
        if self.searchpage.did_we_navigate_to_imac_page():
            self.logger.info("Navigated To Product Display Page")
        else:
            pytest.fail("Not Navigated To Product Display Page")
        # -----------------------------------
        # Back To Search Result
        # -----------------------------------
        time.sleep(3)
        self.driver.back()
        # -----------------------------------
        # GRID VIEW
        # -----------------------------------
        self.searchpage.click_grid_view()
        self.logger.info("Clicked Grid View")
        if self.searchpage.is_display_product_image():
            self.logger.info("Product Image Displayed In Grid View")
        else:
            pytest.fail("Product Not Displayed In Grid View")
        self.searchpage.click_product_image()
        self.logger.info("Clicked Product Name")

        if self.searchpage.did_we_navigate_to_imac_page():
            self.logger.info("Navigated To Product Display Page")
        else:
            pytest.fail("Not Navigated To Product Display Page")

        self.logger.info("========== TC_SF_011 Passed ==========")

    # ==========================================================
    # TC_SF_012
    # Verify List and Grid views when multiple Products
    # are displayed in the search results
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(12)
    def test_list_and_grid_view_multiple_products(self, setup):
        self.logger.info("========== TC_SF_012 Started ==========")
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
        self.homepage = home_page(self.driver)
        self.homepage.enter_product_name("Mac")
        self.homepage.click_search_product()
        self.logger.info("Searched Product : Mac")
        # ------------------------------------------------------
        # Verify Multiple Products Displayed
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        product_count = self.searchpage.get_product_count()
        if product_count > 1:
            self.logger.info(f"Multiple Product Displayed : {product_count}")
        else:
            pytest.fail("Multiple Products Not Displayed")
        # ------------------------------------------------------
        # Click List View
        # ------------------------------------------------------
        self.searchpage.click_list_view()
        self.logger.info("Clicked List View")
        products = self.searchpage.get_all_products_name()
        products_list = []
        for product in products:
            products_list.append(product.text.strip())
        self.logger.info(f"{products_list} are Displayed In List View")
        # ------------------------------------------------------
        # Click List View
        # ------------------------------------------------------
        self.searchpage.click_grid_view()
        self.logger.info("Clicked Grid View")
        products = self.searchpage.get_all_products_name()
        products_list = []
        for product in products:
            products_list.append(product.text.strip())
        self.logger.info(f"{products_list} are Displayed In List View")
        self.logger.info("========== TC_SF_012 Passed ==========")

    # ==========================================================
    # TC_SF_013
    # Verify navigating to Product Compare Page
    # from Search Results page
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(13)
    def test_navigate_to_product_compare_page(self, setup):
        self.logger.info("========== TC_SF_013 Started ==========")
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
        self.homepage = home_page(self.driver)
        self.homepage.enter_product_name("Mac")
        self.homepage.click_search_product()
        self.logger.info("Searched Product : Mac")
        self.searchpage = SearchPage(self.driver)
        # ------------------------------------------------------
        # Click Product Compare Link
        # ------------------------------------------------------
        self.searchpage.click_product_compare_link_text()
        self.logger.info("Clicked Product Compare Link")
        # ------------------------------------------------------
        # Verify Product Compare Page
        # ------------------------------------------------------
        self.productcomparepage = ProductComparePage(self.driver)
        if self.productcomparepage.did_we_navigate_product_compare_page():
            self.logger.info("Navigated To Product Compare Page Successfully")
        else:
            pytest.fail("Failed To Navigate To Product Compare Page")
        self.logger.info("========== TC_SF_013 Passed ==========")

    # ==========================================================
    # TC_SF_014
    # Verify User is able to sort the Products displayed
    # in the Search Results
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(14)
    def test_sort_products_in_search_results(self, setup):
        self.logger.info("========== TC_SF_014 Started ==========")
        self.driver = setup
        self.driver.get(
            ReadConfig.get_application_URL()
        )
        sort_options = [
            "Default",
            "Name (A - Z)",
            "Name (Z - A)",
            "Price (Low > High)",
            "Price (High > Low)",
            "Rating (Highest)",
            "Rating (Lowest)",
            "Model (A - Z)",
            "Model (Z - A)"
        ]

        # ------------------------------------------------------
        # Step 1
        # Open Application
        # ------------------------------------------------------
        self.logger.info("Application Opened Successfully")
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.enter_product_name("Mac")
        self.homepage.click_search_product()
        self.logger.info("Searched Product : Mac")
        self.searchpage = SearchPage(self.driver)
        for option in sort_options:
            self.logger.info(f"Selecting Sort Option : {option}")
            self.searchpage.click_select_sort_option(option)
            time.sleep(2)
            select_option = (self.searchpage.get_selected_sort_option())
            assert select_option == option, (f"Expected: {option}, Actual: {select_option}")
            self.logger.info(f"{option} Selected Successfully")
        self.logger.info("Clicked Select Sort Option")
        self.logger.info("========== TC_SF_014 Passed ==========")

    # ==========================================================
    # TC_SF_015
    # Verify User can select how many products
    # can be displayed in Search Results
    # ==========================================================
    # @pytest.mark.regression
    # @pytest.mark.order(15)
    # def test_select_products_display_count(self, setup):
    #     self.logger.info("========== TC_SF_015 Started ==========")
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
    #     self.homepage = home_page(self.driver)
    #     self.homepage.enter_product_name("Mac")
    #     self.homepage.click_search_product()
    #     self.logger.info("Searched Product : Mac")
    #     self.searchpage = SearchPage(self.driver)
    #     product_count = self.searchpage.get_product_count()
    #     if product_count > 1:
    #         self.logger.info(f"{product_count} Products Displayed")
    #     else:
    #         pytest.fail("Product Not Displayed")
    #
    #     # show_options=self.searchpage.select_show_product_option()
    #     # self.logger.info(f"Total Show Options : {len(show_options.text)}")
    #     # for option in show_options:
    #     #     self.logger.info(f"Selecting Show Option : {option.text}")
    #
    #     all_options = self.searchpage.get_all_show_option()
    #     for option_text in all_options:
    #
    #         self.searchpage.click_show_product_option()
    #         self.logger.info("Show Product Option Displayed")
    #
    #         self.searchpage.select_show_product_option(option_text)
    #         self.logger.info(f"Selected Show Option : {option_text}")
    #         time.sleep(2)
    #
    #         total_products = self.searchpage.get_product_count()
    #         self.logger.info(f"Displayed Products : {total_products}")
    #         if total_products > int(option_text):
    #             CaptureScrenshot.capture_screenshot(self.driver,
    #                                                 f"TC_SF_015_{option_text}")
    #             pytest.fail(f"Displayed Product = {total_products}, Show Values = {option_text}")
    #     self.logger.info("========== TC_SF_015 Passed ==========")
