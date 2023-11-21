from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class PRODUCTPAGE(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    def user_clicks_on_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)

