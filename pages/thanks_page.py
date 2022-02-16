from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class ThanksPage(BaseDriver):
    _thanks_text = (By.CSS_SELECTOR, "div[class='NarrowTitle'] h3")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        if self.is_loaded() is False:
            raise Exception(type(self) + "not loaded")

    def is_loaded(self):
        element = self.wait_for_presence_of_element(self._thanks_text)
        if element:
            return True
        else:
            return False


    def get_thanks(self):
        return self.driver.find_element(self._thanks_text).text
