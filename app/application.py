#from pages.header_page import Header
from pages.header_page import HEADERPAGE
from pages.product_page import PRODUCTPAGE
from pages.main_page import MAINPAGE

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.header_page = HEADERPAGE(self.driver)
        self.product_page = PRODUCTPAGE(self.driver)
        self.main_page = MAINPAGE(self.driver)

