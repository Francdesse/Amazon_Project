from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class SEARCHRESULTSPAGE(Page):
    FRST_PRODUCT = (By.CSS_SELECTOR, '.a-price-whole')

    def clicks_on_first_item(self):
        self.click(*self.FRST_PRODUCT)

    def save_item_name(self):
        self.driver.prd_name = self.driver.find_element(*self.FRST_PRODUCT).text
        print(f'current product: {self.driver.prd_name}')
