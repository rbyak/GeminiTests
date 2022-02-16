import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging


class BaseDriver:
    # This is a driver class that is parent of all pages
    # It contains a generic methods that will be used everywhere
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        logger = logging.getLogger()
        logger.info("Loading [" + type(self)+ "].")

    def load(self, url):
        self.driver.get(url)

    def wait_for_element_and_click(self, locator):
        time.sleep(1)
        element = WebDriverWait(self, 50).until(
            expected_conditions.element_to_be_clickable(self.driver.find_element(locator[0], locator[1])))
        element.click()
        return element

    def wait_for_checkbox_and_click(self, locator):
        time.sleep(1)
        element = WebDriverWait(self, 50).until(
            expected_conditions.element_to_be_clickable(self.driver.find_element(locator[0], locator[1])))
        element.click()
        self.driver.find_element(locator[0], locator[1]).is_selected()
        return element

    def send_keys(self, locator, text):
        element = self.wait_for_element_and_click(locator)
        element.send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return element.text

    def visibility(self, locator):
        element = WebDriverWait(self, 50).until(expected_conditions.visibility_of(locator[0], locator[1]))
        return element

    def is_title_visible(self, title):
        return WebDriverWait(self, 10).until(expected_conditions.title_is(title))

    def title(self):
        return self.driver.title

    def wait_for_presence_of_element(self, locator):
        time.sleep(1)
        locator_element = WebDriverWait(self, 50).until(
            expected_conditions.element_to_be_clickable(self.driver.find_element(locator[0], locator[1])))
        return locator_element

    def wait_for_presence_of_all_element(self, locator):
        locator_element = self.driver.find_element(locator[0], locator[1])
        list_of_element = WebDriverWait(self, 10).until(
            expected_conditions.presence_of_element_located(locator_element))
        return list_of_element

    def get_current_url(self):
        self.driver.current_url()

