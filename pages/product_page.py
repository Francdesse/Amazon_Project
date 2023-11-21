from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class PRODUCTPAGE(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    PRD_TILE = (By.CSS_SELECTOR, '#productTitle')

    def item_open_to_product_page(self, search_item):
        item_tile = self.driver.find_element(*self.PRD_TILE).text
        assert search_item in item_tile, f'Error! {search_item} is not the same as {item_tile}'

    def user_clicks_on_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)

