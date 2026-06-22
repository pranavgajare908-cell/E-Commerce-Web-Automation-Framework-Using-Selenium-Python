from selenium.webdriver.common.by import By


class ProductComparePage:
    def __init__(self, driver):
        self.driver = driver

    # ----------------------------------------
    # TC_SF_013
    product_compare_xpath=(By.XPATH, "//ul[@class='breadcrumb']//a[text()='Product Comparison']")

    def did_we_navigate_product_compare_page(self):
        return self.driver.find_element(*self.product_compare_xpath).is_displayed()