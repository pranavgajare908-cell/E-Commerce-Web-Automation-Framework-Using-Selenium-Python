from selenium.webdriver.common.by import By


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    # ----------------------------------------
    # TC_ATC_001
    get_shopping_cart_product_info_xpath = (By.XPATH,
                                            "//div[@class='table-responsive']//table[@class='table table-bordered']//tbody//tr//td")
    get_quantity = (By.XPATH, "//input[contains(@name,'quantity')]")

    # ----------------------------------------
    # TC_ATC_001
    def get_shopping_cart_product_info(self):
        element = self.driver.find_elements(*self.get_shopping_cart_product_info_xpath)
        return [element.text for element in element]

    def get_product_quantity(self):
        element = self.driver.find_elements(*self.get_quantity)
        return [element.get_attribute("value") for element in element]
