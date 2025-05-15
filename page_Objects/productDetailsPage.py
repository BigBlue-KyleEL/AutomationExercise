from selenium.webdriver.common.by import By

from utilities.browserUtilities import BrowserUtilities


class productDetailsPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.product_name = "Blue Top"
        self.product_name_loc = (By.XPATH, f"//h2[text()='{self.product_name}']")
        self.product_name_text = self.driver.find_element(*self.product_name_loc).text
        self.category = (By.XPATH, "//p[contains(text(),'Category')]")
        self.price = (By.XPATH, f"//h2[text()='{self.product_name_text}']/following-sibling::span/span")
        self.availability = (By.XPATH, "//b[text()='Availability:']")
        self.condition =
        self.brand =


    def verify_productDetailsPage(self):
        BrowserUtilities.wait_for_element_to_appear(self, self.product_name_loc)
        assert self.driver.find_element(*self.product_name_loc).text == self.product_name
        assert self.driver.find_element(*self.category).is_displayed()
        assert self.driver.find_element(*self.price).is_displayed()
        assert self.driver.find_element(*self.price).contains_text(f"{self.product_name_text}")
        assert self.driver.find_element(*self.availability).