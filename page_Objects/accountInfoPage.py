import time

from selenium.webdriver.common.by import By

from utilities.browserUtilities import BrowserUtilities


class accountInfoPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.radio_title1 = (By.ID, "id_gender1")
        self.radio_title2 = (By.ID, "id_gender2")
        self.password = (By.ID, "password")
        self.days_dropdown = (By.ID, "days")
        self.months_dropdown = (By.ID, "months")
        self.years_dropdown = (By.ID, "years")
        self.newsletter_checkbox = (By.ID, "newsletter")
        self.optIN_checkbox = (By.ID, "optin")
        self.firstName_textbox = (By.ID, "first_name")
        self.lastName_textbox = (By.ID, "last_name")
        self.company_textbox = (By.ID, "company")
        self.address_textbox = (By.ID, "address1")
        self.country_dropdown = (By.ID, "country")
        self.state_textbox = (By.ID, "state")
        self.city_textbox = (By.ID, "city")
        self.zipcode_textbox = (By.ID, "zipcode")
        self.mobile_textbox = (By.ID, "mobile_number")
        self.createAccount_btn = (By.XPATH, "//button[@data-qa= 'create-account']")
        self.accountCreated_text = (By.XPATH, "//b[text()= 'Account Created!']")
        self.continue_btn = (By.XPATH, "//a[@data-qa= 'continue-button']")
        self.loggedIn_username = (By.XPATH, "//a[contains(text(), 'Logged in as')]/b")
        self.delete_btn = (By.XPATH, "//a[text()= ' Delete Account']")
        self.accountDeleted_text = (By.XPATH, "//b[text()= 'Account Deleted!']")
        self.logout_btn = (By.XPATH, "//a[text()= ' Logout']")




    def fillUp_infoPage(self, info):
        if info["title"] == "Mr":
            self.driver.find_element(*self.radio_title1).click()
        elif info["title"] == "Mrs":
            self.driver.find_element(*self.radio_title2).click()
        self.driver.find_element(*self.password).send_keys(info["password"])
        birth = info["birth_date"]
        self.driver.find_element(*self.days_dropdown).click()
        self.driver.find_element(By.XPATH, f"//option[@value='{birth["day"]}']").click()
        self.driver.find_element(*self.months_dropdown).click()
        self.driver.find_element(By.XPATH, f"//option[text()='{birth["month"]}']").click()
        self.driver.find_element(*self.years_dropdown).click()
        self.driver.find_element(By.XPATH, f"//option[@value='{birth["year"]}']").click()
        self.driver.find_element(*self.newsletter_checkbox).click()
        self.driver.find_element(*self.optIN_checkbox).click()
        self.driver.find_element(*self.newsletter_checkbox).click()
        self.driver.find_element(*self.firstName_textbox).send_keys(info["first_name"])
        self.driver.find_element(*self.lastName_textbox).send_keys(info["last_name"])
        self.driver.find_element(*self.company_textbox).send_keys(info["company"])
        self.driver.find_element(*self.address_textbox).send_keys(info["address"])
        self.driver.find_element(By.XPATH, f"//option[@value='{info['country']}']").click()
        self.driver.find_element(*self.state_textbox).send_keys(info["state"])
        self.driver.find_element(*self.city_textbox).send_keys(info["city"])
        self.driver.find_element(*self.zipcode_textbox).send_keys(info["zipcode"])
        self.driver.find_element(*self.mobile_textbox).send_keys(info["mobile"])
        BrowserUtilities.wait_for_element_to_appear(self, self.createAccount_btn)
        createAcc_btn_element = self.driver.find_element(*self.createAccount_btn)
        BrowserUtilities.scroll_to_element(self, createAcc_btn_element)
        self.driver.find_element(*self.createAccount_btn).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.accountCreated_text)
        assert self.driver.find_element(*self.accountCreated_text).text == "ACCOUNT CREATED!"
        self.driver.find_element(*self.continue_btn).click()

    def verify_and_delete_account(self, info):
        BrowserUtilities.wait_for_element_to_appear(self, self.loggedIn_username)
        actual_username = self.driver.find_element(*self.loggedIn_username).text
        assert actual_username == info["user_name"]
        self.driver.find_element(*self.delete_btn).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.accountDeleted_text)
        assert self.driver.find_element(*self.accountDeleted_text).text == "ACCOUNT DELETED!"
        self.driver.find_element(*self.continue_btn).click()










