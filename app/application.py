from pages.item_added_to_cart_message_page import ADDEDTOCARTMESSAGEPAGE
from pages.header_page import HEADERPAGE
from pages.product_page import PRODUCTPAGE
from pages.main_page import MAINPAGE
from pages.search_results_page import SEARCHRESULTSPAGE


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header_page = HEADERPAGE(self.driver)
        self.product_page = PRODUCTPAGE(self.driver)
        self.main_page = MAINPAGE(self.driver)
        self.search_results_page = SEARCHRESULTSPAGE(self.driver)
        self.item_added_to_cart_message_page = ADDEDTOCARTMESSAGEPAGE(self.driver)

