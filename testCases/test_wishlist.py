import time

import pytest

from pages.product_wishlist_page import WishlistPage
from utilities.logger import logGen
from utilities.read_properties import ReadConfig
from pages.home_page import home_page
from pages.login_page import loginPage
from pages.product_display_page import ProductDisplayPage
from utilities.screenshot import CaptureScrenshot
from pages.my_account_page import MyAccountPage


class TestWishlist:
    logger = logGen.logger()

    # ==========================================================
    # TC_WL_002
    # Verify adding a product to 'Wish List' page from the
    # Product that is displayed in the 'Related Products'
    # section of 'Product Display' page
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.order(1)
    def test_add_related_product_to_wishlist(self, setup):
        self.logger.info("========== TC_WL_002 Started ==========")

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
        self.homepage.click_my_account()
        self.logger.info("Clicked On My Account")
        # ------------------------------------------------------
        # Click Login
        # ------------------------------------------------------
        self.homepage.click_login()
        # ------------------------------------------------------
        self.loginpage = loginPage(self.driver)
        self.loginpage.enter_e_mail_address("pranavgajare908@gmail.com")
        self.loginpage.enter_password("1234")
        # ------------------------------------------------------
        # Click on Login Button
        # ------------------------------------------------------
        self.loginpage.click_login_button()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # Search Product
        # ------------------------------------------------------
        self.myaccount_page = MyAccountPage(self.driver)
        self.myaccount_page.enter_search_product_name("iMac")
        self.myaccount_page.click_search_product_button()
        self.logger.info("Clicked On Search Product Page")
        # ------------------------------------------------------
        # Navigate to the Product Page
        # ------------------------------------------------------
        self.product_display_page = ProductDisplayPage(self.driver)
        # ------------------------------------------------------
        # Click on Wish-List
        # ------------------------------------------------------
        self.product_display_page.click_wishlist()
        self.logger.info("Clicked On Wishlist Page")
        # ------------------------------------------------------
        # Verify Wishlist Success Message
        # ------------------------------------------------------
        expected_message = "Success: You have added iMac to your wish list!"
        if self.product_display_page.get_wishlist_success_message() == expected_message:
            self.logger.info("Success: You have added iMac to your wish list!")
        else:
            CaptureScrenshot.capture_screenshot(self.driver,
                                                "TC_WL_002_Failed")

        # ------------------------------------------------------
        # Click Wishlist Link
        # ------------------------------------------------------
        self.product_display_page.click_wishlist_link()
        self.logger.info("Clicked On Wishlist Link Page")
        # ------------------------------------------------------
        # Get All Products Wishlist
        # ------------------------------------------------------
        product_wishlist_info = []
        self.product_wishlist_page = WishlistPage(self.driver)
        product_wishlist_info = self.product_wishlist_page.get_all_wishlist_product_info()
        for product_info in product_wishlist_info:
            product_wishlist_info.append(product_info)
            print(product_wishlist_info)
            break
        self.logger.info("========== TC_WL_002 Passed ==========")

    # ==========================================================
    # TC_WL_003
    # Verify adding a product to 'Wish List' page from the
    # Product that is displayed in the 'Featured' section
    # of 'Home' page
    # ==========================================================
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.order(2)
    def test_add_featured_product_to_wishlist(self,setup):
        self.logger.info("========== TC_WL_003 Started ==========")
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
        # ------------------------------------------------------
        self.loginpage = loginPage(self.driver)
        self.loginpage.enter_e_mail_address("pranavgajare908@gmail.com")
        self.loginpage.enter_password("1234")
        self.loginpage.click_login_button()
        self.logger.info("Clicked On Login Page")
        # ------------------------------------------------------
        # Navigate to My Account Page
        # ------------------------------------------------------
        self.myaccount_page = MyAccountPage(self.driver)
        time.sleep(2)
        self.myaccount_page.click_store_logo()
        self.logger.info("Clicked On Store Logo Page")
        # ------------------------------------------------------
        # Navigate to Home Page
        # ------------------------------------------------------
        self.homepage = home_page(self.driver)

        feature_products = [
            "MacBook",
            "iPhone",
            "Apple Cinema 30",
            "Canon EOS 5D"
        ]

        self.driver.execute_script("window.scrollBy(0, 500);")
        product_feature = self.homepage.get_products_feature_name()
        add_to_wish_list =self.homepage.click_product_wish_list()
        for i in range(len(product_feature)):
            if feature_products[0] == product_feature[i]:
                self.logger.info(f"product has been matched {product_feature[i]}")
                add_to_wish_list[i].click()
            break

        expected_message = "Success: You have added MacBook to your wish list!"
        actual_message = self.homepage.get_add_wish_list_success_message()

        if expected_message in actual_message:
            self.logger.info("Wish List Success Message Displayed Successfully")
        else:
            CaptureScrenshot.capture_screenshot(
                self.driver,
                "TC_WL_003_add_to_wish_list_success_message_not_display"
            )
            pytest.fail(f"Expected: {expected_message}\nActual: {actual_message}")

        self.homepage.click_wish_list_add_to_cart()
        self.logger.info("Clicked On Wishlist Page")
        self.wishlist_page = WishlistPage(self.driver)
        wish_list_product = []
        product_wishlist_ = self.wishlist_page.get_all_wishlist_product_info()
        for i in  product_wishlist_:
            wish_list_product.append(i)
            print(product_wishlist_)
            break
        self.logger.info("========== TC_WL_003 Passed ==========")



