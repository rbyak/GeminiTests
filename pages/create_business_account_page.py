from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import BaseDriver
from pages.thanks_page import ThanksPage


class CreateBusinessAccountPage(BaseDriver):

    _company_name_textbox =(By.CSS_SELECTOR, "input[name='company.legalName']")
    _company_type_dropdown = (By.ID, "companyTypeDropdown")
    _country_dropdown = (By.ID, "countryDropdown")
    _state_dropdown = (By.CSS_SELECTOR, ".usStateDropdown__control.css-817ljj-control")
    _legal_first_name_textbox = (By.CSS_SELECTOR, "input[name='personal.legalName.firstName']")
    _label_link = (By.CSS_SELECTOR, ".Label")
    _legal_middle_name_textbox = (By.CSS_SELECTOR, "input[name='personal.legalName.middleName']")
    _legal_last_name_textbox = (By.CSS_SELECTOR, "input[name='personal.legalName.lastName']")
    _email_address_textbox = (By.CSS_SELECTOR, "input[name='personal.email']")
    _agreement_checkbox = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/span[1]/div[1]/label[1]/input[1]")
    _submit_button = (By.CSS_SELECTOR, "button[type='submit']")
    _alert_body = (By.XPATH, "//li[normalize-space()='Legal Business Name is required.']")
    _user_agreement = (By.XPATH, "//a[normalize-space()='User Agreement']")
    _privacy_policy = (By.CSS_SELECTOR, '[data-testid="unitedStatesPrivacyPolicy"]')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        if self.is_loaded() is False:
            raise Exception(type(self) + "not loaded")

    def is_loaded(self):
        element = self.wait_for_presence_of_element(self._company_type_dropdown)
        if element:
            return True
        else:
            return False

    def set_company_name(self, company_name):
        self.send_keys(self._company_name_textbox, company_name)

    def choose_company_type(self,company_type):
        self.wait_for_element_and_click(self._company_type_dropdown)
        self.wait_for_element_and_click((By.ID, company_type.value))

    def choose_country_type(self,country_name):
        self.wait_for_element_and_click(self._country_dropdown)
        self.wait_for_element_and_click((By.ID, country_name.value))

    def set_legal_first_name(self, first_name):
        self.send_keys(self._legal_first_name_textbox, first_name)

    def set_legal_middle_name(self, middle_name):
        self.send_keys(self._legal_middle_name_textbox, middle_name)

    def set_legal_last_name(self, last_name):
        self.send_keys(self._legal_last_name_textbox, last_name)

    def set_email_address(self, email_address):
        self.send_keys(self._email_address_textbox, email_address)

    def set_agreement_checkbox(self):
        element = self.driver.find_element(self._agreement_checkbox[0], self._agreement_checkbox[1])
        element.click()

    def click_submit(self):
        self.wait_for_element_and_click(self._submit_button)
        return ThanksPage(self)

    def click_submit_expecting_error(self):
        self.wait_for_element_and_click(self._submit_button)
        self.wait_for_presence_of_element(self._alert_body)

    def is_alert_present(self, errorText):
        self.wait_for_element_and_click(self._submit_button)
        element = self.wait_for_presence_of_element(self._alert_body)
        return element.get_text.__eq__(errorText)

    def click_User_agreement_and_return_url(self):
        self.wait_for_element_and_click(self._user_agreement)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.get_current_url()

    def click_privacy_policy_return_url(self):
        self.wait_for_element_and_click(self._privacy_policy)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.get_current_url()

    def get_title(self):
        return self.title()
