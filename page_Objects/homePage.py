import os
import time

from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By

from page_Objects.accountInfoPage import accountInfoPage
from utilities.browserUtilities import BrowserUtilities


class homePage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.carousel = (By.ID, "slider-carousel")
        self.signUp_btn1 = (By.XPATH, "//a[text()=' Signup / Login']")
        self.newUser_txt = (By.XPATH, "//h2[text()='New User Signup!']")
        self.signUp_Name_textbox = (By.XPATH, "//input[@data-qa='signup-name']")
        self.signUp_Email_textbox = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signUp_btn2 = (By.XPATH, "//button[@data-qa='signup-button']")
        self.accountInfo_txt = (By.XPATH, "//b[text()='Enter Account Information']")
        self.login_email_textbox = (By.XPATH, "//input[@data-qa='login-email']")
        self.login_password_textbox = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_btn = (By.XPATH, "//button[@data-qa='login-button']")
        self.incorrect_credentials = (By.XPATH, "//p[text()='Your email or password is incorrect!']")
        self.existing_email = (By.XPATH, "//p[text()='Email Address already exist!']")
        self.contact_us_btn = (By.XPATH, "//a[text()=' Contact us']")
        self.get_in_touch_txt = (By.XPATH, "//h2[text()='Get In Touch']")
        self.contactUs_Name_textbox = (By.XPATH, "//input[@data-qa='name']")
        self.contactUs_Email_textbox = (By.XPATH, "//input[@data-qa='email']")
        self.contactUs_Subject_textbox = (By.XPATH, "//input[@data-qa='subject']")
        self.contactUs_Message_textbox = (By.XPATH, "//textarea[@data-qa='message']")
        self.contactUs_fileUpload = (By.XPATH, "//input[@name='upload_file']")
        self.contactUs_submit_btn = (By.XPATH, "//input[@data-qa='submit-button']")
        self.contactUs_successMsg = (By.XPATH, "//div[@class='status alert alert-success']")
        self.contactUs_home_btn = (By.XPATH, "//a[@class='btn btn-success']")
        self.testCases_btn = (By.XPATH, "//a[text()=' Test Cases']")
        self.testCases_title = (By.XPATH, "//b[text()='Test Cases']")
        self.products_btn = (By.XPATH, "//a[text()=' Products']")
        self.products_title = (By.XPATH, "//h2[text()='All Products']")
        cardNumber = 1
        self.products_card = (By.XPATH, f"//div[@class='col-sm-4'][{cardNumber}]")
        self.products_view_btn = (By.XPATH, "(//div[@class='choose']//ul//li//a)[1]")
        self.products_addToCart_btn = (By.XPATH, f"//div[@class='col-sm-4'][{cardNumber}]//a[text()=' Add to cart']")
        self.products_itemAdded_text = (By.XPATH, "//h4[@class='modal-title w-100']")
        self.products_modal_confirmBtn = (By.XPATH, "//button[@data-dismiss='modal']")

    def verify_homePage(self):
        BrowserUtilities.wait_for_element_to_appear(self, self.carousel)
        assert self.driver.find_element(*self.carousel).is_displayed()

    def register_user(self, info):
        self.driver.find_element(*self.signUp_btn1).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.newUser_txt)
        assert self.driver.find_element(*self.newUser_txt).text == "New User Signup!"
        self.driver.find_element(*self.signUp_Name_textbox).send_keys(info["user_name"])
        self.driver.find_element(*self.signUp_Email_textbox).send_keys(info["email"])
        self.driver.find_element(*self.signUp_btn2).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.accountInfo_txt)
        assert self.driver.find_element(*self.accountInfo_txt).text == "ENTER ACCOUNT INFORMATION"
        accountInfo_Page = accountInfoPage(self.driver)
        return accountInfo_Page

    def login_w_correct_credentials(self, info):
        BrowserUtilities.wait_for_element_to_appear(self, self.newUser_txt)
        assert self.driver.find_element(*self.newUser_txt).text == "New User Signup!"
        self.driver.find_element(*self.login_email_textbox).send_keys(info["email"])
        self.driver.find_element(*self.login_password_textbox).send_keys(info["password"])
        self.driver.find_element(*self.login_btn).click()

    def login_w_incorrect_credentials(self, info):
        BrowserUtilities.wait_for_element_to_appear(self, self.newUser_txt)
        assert self.driver.find_element(*self.newUser_txt).text == "New User Signup!"
        self.driver.find_element(*self.login_email_textbox).send_keys(info["incorrect_email"])
        self.driver.find_element(*self.login_password_textbox).send_keys(info["incorrect_password"])
        self.driver.find_element(*self.login_btn).click()

    def contact_us(self, info):
        BrowserUtilities.wait_for_element_to_appear(self, self.contact_us_btn)
        self.driver.find_element(*self.contact_us_btn).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.get_in_touch_txt)
        assert self.driver.find_element(*self.get_in_touch_txt).text == "GET IN TOUCH"
        self.driver.find_element(*self.contactUs_Name_textbox).send_keys(info["name"])
        self.driver.find_element(*self.contactUs_Email_textbox).send_keys(info["email"])
        self.driver.find_element(*self.contactUs_Subject_textbox).send_keys(info["subject"])
        self.driver.find_element(*self.contactUs_Message_textbox).send_keys(info["message"])
        file_path = os.path.abspath(info["file_path"])
        self.driver.find_element(*self.contactUs_fileUpload).send_keys(file_path)
        file_upload_value = self.driver.find_element(*self.contactUs_fileUpload).get_attribute("value")
        assert info["file_name"] in file_upload_value
        self.driver.find_element(*self.contactUs_submit_btn).click()
        popup_alert = BrowserUtilities.wait_for_alert(self)
        assert "Press OK to proceed!" in popup_alert.text
        popup_alert.accept()
        BrowserUtilities.wait_for_element_to_appear(self, self.contactUs_successMsg)
        assert self.driver.find_element(*self.contactUs_successMsg).text == "Success! Your details have been submitted successfully."
        self.driver.find_element(*self.contactUs_home_btn).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.carousel)
        assert self.driver.find_element(*self.carousel).is_displayed()

    def verify_TestCases_page(self):
        BrowserUtilities.wait_for_element_to_appear(self, self.testCases_btn)
        self.driver.find_element(*self.testCases_btn).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.testCases_title)
        assert self.driver.find_element(*self.testCases_title).text == "TEST CASES"

    def verify_productsDetailPage(self):
        BrowserUtilities.wait_for_element_to_appear(self, self.products_btn)
        self.driver.find_element(*self.products_btn).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.products_title)
        assert self.driver.find_element(*self.products_title).text == "ALL PRODUCTS"
        self.driver.find_element(*self.products_card)
        self.driver.find_element(*self.products_view_btn).click()
        assert "Automation Exercise - Product Details" in self.driver.title
        


    def productPage_addToCart(self):
        BrowserUtilities.wait_for_element_to_appear(self, self.products_btn)
        self.driver.find_element(*self.products_btn).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.products_title)
        assert self.driver.find_element(*self.products_title).text == "ALL PRODUCTS"
        BrowserUtilities.hover_to_element(self, self.products_card)
        BrowserUtilities.wait_for_element_to_be_clickable(self, self.products_addToCart_btn)
        self.driver.find_element(*self.products_addToCart_btn).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.products_itemAdded_text)
        assert self.driver.find_element(*self.products_itemAdded_text).text == "Added!"
        self.driver.find_element(*self.products_modal_confirmBtn).click()
        # TBC






    def test_pageObject(self):
        self.driver.find_element(*self.signUp_btn1).click()
        BrowserUtilities.wait_for_element_to_appear(self, self.newUser_txt)
        assert self.driver.find_element(*self.newUser_txt).text == "New User Signup!"

