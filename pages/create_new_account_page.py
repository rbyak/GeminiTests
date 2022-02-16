import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.create_business_account_page import CreateBusinessAccountPage


class CreateNewAccountPage(BaseDriver):
    url = 'https://exchange.sandbox.gemini.com/register'

    create_business_account_button = (By.CSS_SELECTOR, '[data-testid="register-go-to-institution-register"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        if self.is_loaded() is False:
            raise Exception(type(self) + "not loaded")

    def is_loaded(self):
        element = self.wait_for_presence_of_element(self.create_business_account_button)
        if element:
            return True
        else:
            return False

    def click_create_business_account(self):
        time.sleep(3)
        self.wait_for_element_and_click(self.create_business_account_button)
        return CreateBusinessAccountPage(self.driver)

    def get_title(self):
        return self.title()

