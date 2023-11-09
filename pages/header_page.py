from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class HEADERPAGE(Page):
    SEARCH_BOX= (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_BTN= (By.ID, "nav-search-submit-button")
    SEARCH_RESULTS_IN_QUOTE= (By.CSS_SELECTOR, '.sg-col-inner .a-color-state.a-text-bold')

    def user_searches_for_airpods(self, search_item):
        self.input_text(search_item, *self.SEARCH_BOX)

    def user_clicks_search_btn(self):
        self.click(*self.SEARCH_BTN)

    def user_sees_airpods_in_search_results(self,expected_result):
        self.verify_element_text(expected_result,*self.SEARCH_RESULTS_IN_QUOTE), 'Tile in quotes is missing'