import time

import pytest

from pages.product_wishlist_page import WishlistPage
from pages.show_all_products import ShowAllProductsPage
from utilities.logger import logGen
from pages.home_page import home_page
from utilities.read_properties import ReadConfig
from pages.search_page import SearchPage
from pages.product_display_page import ProductDisplayPage
from utilities.screenshot import CaptureScrenshot
from pages.shopping_cart_page import ShoppingCartPage
from pages.login_page import loginPage
from pages.my_account_page import MyAccountPage


class TestAddToCart:
    logger = logGen.logger()

    # ==========================================================
    # TC_ATC_001
    # Verify adding the product to
    # Cart from 'Product Display' Page
    # ==========================================================
    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_add_product_to_cart_from_product_display_page(self, setup):
        self.logger.info("========== TC_ATC_001 Started ==========")
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
        self.logger.info("Product Search Clicked")
        # ------------------------------------------------------
        # Click on the Product displayed in the Search results
        # ------------------------------------------------------
        self.searchpage = SearchPage(self.driver)
        self.searchpage.click_display_product_image()
        self.logger.info("Display Product Image Clicked")
        # ------------------------------------------------------
        # Click on 'Add to Cart' button in the displayed 'Product Display' page
        # ------------------------------------------------------
        self.product_page = ProductDisplayPage(self.driver)
        self.product_page.click_add_to_cart()
        self.logger.info("Add Product Clicked")
        # ------------------------------------------------------
        # ER-1 Verify Success Message
        # ------------------------------------------------------
        expected_message = "Success: You have added iMac to your shopping cart!"
        try:
            if self.product_page.get_add_to_cart_success_message() == expected_message:
                self.logger.info(f"{expected_message} Successfully Displayed")
        except AssertionError:
            CaptureScrenshot.capture_screenshot(self.driver, "TC_ATC_001_add_to_cart_success_message_not_display")
            pytest.fail("Add To Cart Success Message Not Displayed....")

        # ------------------------------------------------------
        # Click on the 'shopping cart!' link in the displayed success message
        # ------------------------------------------------------
        time.sleep(3)
        self.product_page.click_shopping_cart()
        self.logger.info("Shopping Cart Clicked")
        # ------------------------------------------------------
        # ER-2
        # Product should be successfully displayed in the 'Shopping Cart' page
        # ------------------------------------------------------
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_info = self.shopping_cart_page.get_shopping_cart_product_info()
        product_quantity = self.shopping_cart_page.get_product_quantity()
        for product_info in shopping_cart_info:
            print(f"Product Info : {product_info} | Quantity : {product_quantity}")
        self.logger.info("========== TC_ATC_001 Passed ==========")

    # ==========================================================
    # TC_ATC_002
    # Verify adding the product to Cart from 'Wish List' Page
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_add_product_to_cart_from_wishlist(self, setup):
        self.logger.info("========== TC_ATC_002 Started ==========")
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
        # Click My Account
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        self.homepage.click_login()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        self.loginPage = loginPage(self.driver)
        self.loginPage.enter_e_mail_address("pranavgajare908@gmail.com")
        self.loginPage.enter_password("1234")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.loginPage.click_login_button()
        self.logger.info("User Logged In Successfully")
        # ------------------------------------------------------
        self.my_account_page = MyAccountPage(self.driver)
        self.my_account_page.enter_search_product_name("iMac")
        self.my_account_page.click_search_product_button()
        self.logger.info("Search Product Button Clicked")
        # ------------------------------------------------------
        # Navigate to the Product Display Page
        # ------------------------------------------------------
        self.product_page = ProductDisplayPage(self.driver)
        self.product_page.click_product_wishlist()
        self.logger.info("Product Wishlist Clicked")
        self.product_page.click_wishlist_header()
        self.logger.info("Product Wishlist Header Clicked")
        # ------------------------------------------------------
        # Navigate to the Product Wishlist Page
        # ------------------------------------------------------
        self.wishlist_page = WishlistPage(self.driver)
        self.wishlist_page.click_wishlist_add_to_cart_button()
        self.logger.info("Wishlist Add To Cart Clicked")
        self.wishlist_page.click_shopping_cart_header()
        self.logger.info("Shopping Cart Header Clicked")
        # ------------------------------------------------------
        # Navigate to the Shopping Cart Page
        # ------------------------------------------------------
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_info = self.shopping_cart_page.get_shopping_cart_product_info()
        product_quantity = self.shopping_cart_page.get_product_quantity()
        for product_info in shopping_cart_info:
            print(f"Product Info : {product_info} | Quantity : {product_quantity}")

        self.logger.info("========== TC_ATC_002 Passed ==========")

    # ==========================================================
    # TC_ATC_003
    # Verify adding the product to Cart from Search Results Page
    # ==========================================================
    @pytest.mark.sanity
    @pytest.mark.order(3)
    def test_add_product_to_cart_from_search_results_page(self, setup):
        self.logger.info("========== TC_ATC_003 Started ==========")
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
        self.logger.info("Search Product Button Clicked")
        # ------------------------------------------------------
        # Navigate to Product Page
        # ------------------------------------------------------
        self.product_page = ProductDisplayPage(self.driver)
        self.product_page.click_add_to_cart()
        self.logger.info("Add Product Button Clicked")
        if self.product_page.get_add_to_cart_success_message():
            self.logger.info("Product Have Benn Added Successfully Validated")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_ATC_003")
            pytest.fail("Product Added Not Displayed")
        # ------------------------------------------------------
        # Click Cart Button
        # ------------------------------------------------------
        self.product_page.click_cart_button()
        self.logger.info("Clicked On Cart Button Clicked")
        self.product_page.click_cart_button()
        self.logger.info("Clicked On Cart Button Clicked")
        time.sleep(2)
        self.product_page.click_view_cart()
        self.logger.info("Clicked On Cart Button Clicked")
        # ------------------------------------------------------
        # Navigate to Shopping Cart Page
        # ------------------------------------------------------
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_info = self.shopping_cart_page.get_shopping_cart_product_info()
        product_quantity = self.shopping_cart_page.get_product_quantity()
        for product_info in shopping_cart_info:
            print(f"Product Info : {product_info} | Quantity : {product_quantity}")

        self.logger.info("========== TC_ATC_003 Finished ==========")

    # ==========================================================
    # TC_ATC_005
    # Verify adding the product to Cart from the Products
    # displayed in the category or sub-category page
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_add_product_to_cart_from_category_page(self, setup):
        self.logger.info("========== TC_ATC_00 Started ==========")
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
        self.homepage.click_hover_desktop_menu()
        self.logger.info("Hover Desktop Menu Clicked")
        self.homepage.click_show_all_desktops()
        self.logger.info("Show All Desktops Clicked")
        # ------------------------------------------------------
        # Navigate to Show All Products
        # ------------------------------------------------------
        self.show_all_product = ShowAllProductsPage(self.driver)
        self.show_all_product.click_product_sub_categories()
        self.logger.info("Show All Products Clicked")
        self.show_all_product.click_product_sub_categoies_add_to_cart()
        self.logger.info("Product Added to the Cart Clicked")
        if self.show_all_product.get_add_to_cart_success_message():
            self.logger.info("Product Have Benn Added Successfully Validated")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_ATC_005_Failed")
            pytest.fail("Product Added Not Displayed")
        self.show_all_product.click_shopping_cart()
        self.logger.info("Clicked On Cart Button Clicked")
        # ------------------------------------------------------
        # Navigate to Shopping Cart
        # ------------------------------------------------------
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_info = self.shopping_cart_page.get_shopping_cart_product_info()
        product_quantity = self.shopping_cart_page.get_product_quantity()
        for product_info in shopping_cart_info:
            print(f"Product Info : {product_info} | Quantity : {product_quantity}")
        self.logger.info("========== TC_ATC_005 Finished ==========")

    # ==========================================================
    # TC_ATC_006
    # Verify adding the product to Cart from the Products
    # displayed in the 'Featured' section of Home page
    # ==========================================================
    @pytest.mark.sanity
    @pytest.mark.order(5)
    def test_add_product_to_cart_from_featured_products(self, setup):
        self.logger.info("========== TC_ATC_06 Started ==========")
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
        feature_products = [
            "MacBook",
            "iPhone",
            "Apple Cinema 30",
            "Canon EOS 5D"
        ]
        products_features = self.homepage.get_products_feature_name()
        add_to_cart_button = self.homepage.click_product_feature_add_to_cart()
        for i in range(len(products_features)):
            if feature_products[0] == products_features[i]:
                self.logger.info(f"product has been matched {products_features[i]}")
                add_to_cart_button[i].click()
            break

        expected_message = "Success: You have added iMac to your shopping cart!"
        try:
            if self.homepage.get_add_to_cart_success_message() == expected_message:
                self.logger.info(f"{expected_message} Successfully Displayed")
        except AssertionError:
            CaptureScrenshot.capture_screenshot(self.driver, "TC_ATC_001_add_to_cart_success_message_not_display")
            pytest.fail("Add To Cart Success Message Not Displayed....")

        self.homepage.click_add_to_cart()
        time.sleep(2)
        self.logger.info("Clicked On Cart Button Clicked")
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_info = self.shopping_cart_page.get_shopping_cart_product_info()
        product_quantity = self.shopping_cart_page.get_product_quantity()
        for product_info in shopping_cart_info:
            print(f"Product Info : {product_info} | Quantity : {product_quantity}")
        self.logger.info("========== TC_ATC_006 Finished ==========")
