from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class SEARCHRESULTSPAGE(Page):
    FRST_PRODUCT = (By.CSS_SELECTOR, '.a-section .a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2 ')
    PRD_TILE = (By.CSS_SELECTOR, '#productTitle')

    def clicks_on_first_item(self):
        clicking_frst_item = self.wait.until(EC.element_to_be_clickable(self.FRST_PRODUCT))
        clicking_frst_item.click()

    def save_item_name(self):
        self.driver.prd_name = self.driver.find_element(*self.FRST_PRODUCT).text
        print(f'current product: {self.driver.prd_name}')

    def item_open_to_product_page(self, search_item):
        item_tile = self.driver.find_element(*self.FRST_PRODUCT).text
        assert search_item in item_tile, f'Error! {search_item} is not the same as {item_tile}'