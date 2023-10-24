from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MAINPAGE(Page):


    def user_nav_to_Amz_website(self):
        self.open_url('https://www.amazon.com/')