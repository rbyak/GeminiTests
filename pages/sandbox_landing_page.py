import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.create_new_account_page import CreateNewAccountPage


class SandboxLandingPage(BaseDriver):
    create_new_account_link = (By.CSS_SELECTOR, '[data-testid="goToRegister"]')
    forgot_password_link = (By.CSS_SELECTOR, '[data-testid="goToResetPassword"]')
    email_address_input_textbox = (By.CSS_SELECTOR, '[data-testid="emailAddressInput"]')
    password_input_textbox = (By.CSS_SELECTOR, '[data-testid="passwordInput"]')
    remember_my_email_address_checkbox = (By.CSS_SELECTOR, '.css-1yfjfjg.e7imnfz0')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        if self.is_loaded() is False:
            raise Exception(type(self) + "not loaded")

    def is_loaded(self):
        element = self.wait_for_presence_of_element(self.email_address_input_textbox)
        if element:
            return True
        else:
            return False

    def click_create_new_account(self):
        self.wait_for_element_and_click(self.create_new_account_link)
        time.sleep(5)
        return CreateNewAccountPage(self.driver)

    def get_title(self):
        return self.title()
