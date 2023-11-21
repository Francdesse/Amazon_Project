from selenium.webdriver.common.by import By
from pages.base_page import Page


class ADDEDTOCARTMESSAGEPAGE(Page):
    ADDED_TO_CART_MESSAGE = (By.ID, 'NATC_SMART_WAGON_CONF_MSG_SUCCESS')

    def verify_add_to_crt_message(self):
        assert self.find_element(*self.ADDED_TO_CART_MESSAGE).text,f"Error! Not correct message"