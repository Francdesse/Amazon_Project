from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class HEADERPAGE(Page):
    SEARCH_BOX= (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_BTN= (By.ID, "nav-search-submit-button")
    SEARCH_RESULTS_IN_QUOTE= (By.CSS_SELECTOR, '.sg-col-inner .a-color-state.a-text-bold')
    CART= (By.ID, 'nav-cart-count-container')

    CART_COUNT=(By.CSS_SELECTOR, '#nav-cart-count-container .nav-cart-count')

    def user_searches_for_airpods(self, search_item):
        self.input_text(search_item, *self.SEARCH_BOX)

    def user_clicks_search_btn(self):
        self.click(*self.SEARCH_BTN)

    def user_sees_airpods_in_search_results(self,expected_result):
        self.verify_element_text(expected_result,*self.SEARCH_RESULTS_IN_QUOTE), 'Tile in quotes is missing'

    def item_is_in_cart(self, expected_result):
        self.verify_element_text(expected_result, *self.ITEM_IN_CART), 'Item title is not found'

    def user_clicks_on_cart(self):
        self.click(*self.CART), 'Cart is not functional'

    def num_on_cart_item(self, cart_numb):
        sleep(2)
        self.verify_element_text(cart_numb, *self.CART_COUNT), f'Error, numbers not the same'

