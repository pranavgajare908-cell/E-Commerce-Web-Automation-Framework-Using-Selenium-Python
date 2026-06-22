from selenium.webdriver.common.by import By
from pages.shopping_cart_page import ShoppingCartPage


class WishlistPage:
    def __init__(self, driver):
        self.driver = driver

    # ----------------------------------------
    # TC_ATC_002
    wishlist_add_to_cart_button_xpath = (By.XPATH,
                                         "//table[@class='table table-bordered table-hover']//tbody//td[@class='text-right']//button[@type='button']//i[@class='fa fa-shopping-cart']")
    shopping_cart_header_xpath = (By.XPATH, "//a[@title='Shopping Cart']")

    # ----------------------------------------
    # TC_WL_002
    wish_list_product_info_xpath = (By.XPATH,
                                    "(//div[contains(@class,'table-responsive')]//table[contains(@class,'table')]//tbody/tr[1]/td)[position()<=5]")

    # ----------------------------------------
    # TC_ATC_002
    def click_wishlist_add_to_cart_button(self):
        self.driver.find_element(*self.wishlist_add_to_cart_button_xpath).click()

    def click_shopping_cart_header(self):
        self.driver.find_element(*self.shopping_cart_header_xpath).click()
        return ShoppingCartPage(self.driver)

    # ----------------------------------------
    # TC_WL_002
    def get_all_wishlist_product_info(self):
        elements = self.driver.find_elements(*self.wish_list_product_info_xpath)
        return[element.text for element in elements]
