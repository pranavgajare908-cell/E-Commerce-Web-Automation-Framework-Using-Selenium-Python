from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.product_compare_page import ProductComparePage
from pages.product_display_page import ProductDisplayPage


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    # ----------------------------------------
    # TC_SF_001
    product_info = (By.XPATH,
                    "//div[@class='caption']//p[text()='Just when you thought iMac had everything, now there´s even more. More powerful Intel Core 2 Duo pro..']")

    # ----------------------------------------
    # TC_SF_002
    warning_product_message = (By.XPATH,
                               "//div[@id='content']//p[text()='There is no product that matches the search criteria.']")

    # ----------------------------------------
    # TC_SF_004
    is_navigate_product_page = (By.XPATH, "//div[@class='product-thumb']")

    # ----------------------------------------
    # TC_SF_004
    keyword_criteria_placeholder = (By.XPATH, "//input[@placeholder='Keywords']")

    # ----------------------------------------
    # TC_SF_007
    search_product_criteria = (By.XPATH, "//input[@id='input-search']")
    search_button = (By.XPATH, "//input[@id='button-search']")

    # ----------------------------------------
    # TC_SF_008
    check_search_product_description = (By.XPATH, "//input[@name='description'][@value='1']")
    search_product_description = (By.XPATH, "//h1[contains(text(),'iMac Product')]")

    # ----------------------------------------
    # TC_SF_009
    click_category_dropdown = (By.XPATH, "//select[@name='category_id']")
    drp_category = (By.XPATH, "//select[@name='category_id']")
    no_product_warning_message = (By.XPATH, "//input[@id='button-search']/following-sibling::p")

    # ----------------------------------------
    # TC_SF_010
    subcategory_chkbox = (By.XPATH, "//input[@name='sub_category'][@value='1']")
    products = (By.XPATH, "//div[@class='product-thumb']")

    # ----------------------------------------
    # TC_SF_011
    list_view = (By.XPATH, "//button[@id='list-view']")
    grid_view = (By.XPATH, "//button[@id='grid-view']")
    display_product_image = (By.XPATH, "//a/img[@title='iMac']")
    navigate_to_iMac_page = (By.XPATH, "//ul[@class='breadcrumb']//a[text()='iMac']")

    # ----------------------------------------
    # TC_SF_012
    product_count = (By.XPATH, "//div[@class='product-thumb']")
    products_name = (By.XPATH, "//div[contains(@class,'product-thumb')]//h4/a")

    # ----------------------------------------
    # TC_SF_013
    product_compare_xpath = (By.LINK_TEXT, "Product Compare (0)")

    # ----------------------------------------
    # TC_SF_014
    sort_product_dropdown = (By.XPATH, "//select[@id='input-sort']")

    # ----------------------------------------
    # TC_SF_015
    show_product_number = (By.XPATH, "//select[@id='input-limit']")

    # ----------------------------------------
    # TC_SF_001
    def get_product_info(self):
        return self.driver.find_element(*self.product_info).text

    # ----------------------------------------
    # TC_SF_002
    def get_warning_product_message(self):
        try:
            return self.driver.find_element(*self.warning_product_message).text
        except NoSuchElementException:
            return False

    # ----------------------------------------
    # TC_SF_004
    def did_navigate_to_product_page(self):
        try:
            return self.driver.find_element(*self.is_navigate_product_page).is_displayed()
        except NoSuchElementException:
            return False

    # ----------------------------------------
    # TC_SF_004
    def get_search_result_count(self):
        return len(self.driver.find_elements(*self.is_navigate_product_page))

    # ----------------------------------------
    # TC_SF_004
    def get_keyword_criteria_placeholder(self):
        return self.driver.find_element(*self.keyword_criteria_placeholder).get_attribute("placeholder")

    # ----------------------------------------
    # TC_SF_007
    def enter_search_product_criteria(self, search_product_criteria):
        return self.driver.find_element(*self.search_product_criteria).send_keys(search_product_criteria)

    def click_search_button(self):
        button = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.presence_of_element_located(
                self.search_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # ----------------------------------------
    # TC_SF_008
    def click_check_search_product_description(self):
        return self.driver.find_element(*self.check_search_product_description).click()

    def get_search_product_description(self):
        return self.driver.find_element(*self.search_product_description).is_displayed()

    # ----------------------------------------
    # TC_SF_009
    # def click_category_drop(self):
    # return self.driver.find_element(*self.click_category_dropdown).click()

    def select_drp_category(self):
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.drp_category)
            )
            select = Select(dropdown)
            return select.options
        except NoSuchElementException:
            return False

    def is_no_product_warning_message(self):
        try:
            return self.driver.find_element(*self.no_product_warning_message).is_displayed()
        except:
            return False

    def print_categories(self):

        dropdown = Select(
            self.driver.find_element(
                *self.drp_category
            )
        )
        for option in dropdown.options:
            print(option.text)

    # ----------------------------------------
    # TC_SF_010
    def click_subcategory_chkbox(self):
        return self.driver.find_element(*self.subcategory_chkbox).click()

    # ----------------------------------------
    # TC_SF_011
    def click_list_view(self):
        return self.driver.find_element(*self.list_view).click()

    def click_grid_view(self):
        return self.driver.find_element(*self.grid_view).click()

    def is_display_product_image(self):
        return self.driver.find_element(*self.display_product_image).is_displayed()

    def click_product_image(self):
        return self.driver.find_element(*self.display_product_image).click()

    def did_we_navigate_to_imac_page(self):
        try:
            return self.driver.find_element(*self.navigate_to_iMac_page).is_displayed()
        except NoSuchElementException:
            return False

    # ----------------------------------------
    # TC_SF_012
    def get_product_count(self):
        return len(self.driver.find_elements(*self.product_count))

    def get_all_products_name(self):
        return self.driver.find_elements(*self.products_name)

    # ----------------------------------------
    # TC_SF_013
    def click_product_compare_link_text(self):
        self.driver.find_element(*self.product_compare_xpath).click()
        return ProductComparePage(self.driver)

    # ----------------------------------------
    # TC_SF_014
    def click_select_sort_option(self, option_text):
        dropdown = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.sort_product_dropdown
            )
        )
        dropdown.click()
        Select(dropdown).select_by_visible_text(
            option_text
        )

    def get_selected_sort_option(self):
        dropdown = self.driver.find_element(
            *self.sort_product_dropdown
        )
        return Select(
            dropdown
        ).first_selected_option.text.strip()

    # ----------------------------------------
    # TC_SF_015
    # def click_show_product_option(self):
    #     dropdown = WebDriverWait(
    #         self.driver,
    #         10
    #     ).until(
    #         EC.presence_of_element_located(
    #             self.show_product_number
    #         )
    #     )
    #     dropdown.click()
    #     return Select(dropdown).options
    #
    # def get_all_show_option(self):
    #     dropdown = (self.driver.find_element
    #         (
    #         *self.show_product_number)
    #     )
    #     select = Select(dropdown)
    #     return [
    #         option.text.strip()
    #         for option in select.options
    #     ]
    #
    # def select_show_product_option(self,option_text):
    #     dropdown = WebDriverWait(
    #         self.driver,
    #         10
    #     ).until(
    #         EC.presence_of_element_located(
    #             self.show_product_number
    #         )
    #     )
    #     Select(
    #         dropdown
    #     ).select_by_visible_text(
    #         option_text
    #     )

    # ----------------------------------------
    # TC_ATC_001
    def click_display_product_image(self):
        self.driver.find_element(*self.display_product_image).click()
        return ProductDisplayPage(self.driver)

