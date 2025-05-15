from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BrowserUtilities:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_appear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def wait_for_element_to_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def wait_for_alert(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(ec.alert_is_present())
            return self.driver.switch_to.alert
        except TimeoutException:
            raise AssertionError("Alert did not appear within the given time.")

    def hover_to_element(self, element):
        try:
            action = self.driver.action_chains
            action.move_to_element(element).perform()
        except TimeoutException:
            raise AssertionError("Element did not appear within the given time.")