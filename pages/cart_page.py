from selenium.webdriver.common.by import By
from pages.base_page import Page


class CARTPAGE(Page):
    ITEM_IN_CART = (By.CSS_SELECTOR, '.sc-item-product-title-cont')

    def item_is_in_cart(self, expected_result):
        prd_title= self.driver.find_element(*self.ITEM_IN_CART).text
        assert expected_result in prd_title, f'Error {expected_result} is not in {prd_title}'