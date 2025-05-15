import time

from selenium.webdriver.common.by import By

from page_Objects.accountInfoPage import accountInfoPage
from page_Objects.homePage import homePage
from utilities.browserUtilities import BrowserUtilities

user_info = {
        "user_name": "test_AE001",
        "title": "Mrs",
        "first_name": "Clark",
        "last_name": "Kent",
        "company": "Daily Planet",
        "email": "clark@dailyplanet.com",
        "incorrect_email": "clark@dailyplanet",
        "incorrect_password": "superman",
        "password": "superman123",
        "address": "1007 Mountain Drive",
        "city": "Metropolis",
        "state": "NY",
        "zipcode": "54321",
        "country": "United States",
        "mobile": "1234567890",
        "birth_date": {
            "day": "27",
            "month": "May",
            "year": "1997"
        }
    }

def test_AE001(browserInstance):
    driver = browserInstance
    home_Page = homePage(driver)
    home_Page.verify_homePage()
    accountInfo_Page = home_Page.register_user(user_info)
    accountInfo_Page.fillUp_infoPage(user_info)
    accountInfo_Page.verify_and_delete_account(user_info)

def test_AE002(browserInstance):
    driver = browserInstance
    home_Page = homePage(driver)
    home_Page.verify_homePage()
    accountInfo_Page = home_Page.register_user(user_info)
    accountInfo_Page.fillUp_infoPage(user_info)
    accountInfo_Page.wait_for_element_to_appear(accountInfo_Page.logout_btn)
    driver.find_element(*accountInfo_Page.logout_btn).click()
    home_Page.login_w_correct_credentials(user_info)
    accountInfo_Page.verify_and_delete_account(user_info)

def test_AE003(browserInstance):
    driver = browserInstance
    home_Page = homePage(driver)
    home_Page.verify_homePage()
    home_Page.wait_for_element_to_appear(home_Page.signUp_btn1)
    driver.find_element(*home_Page.signUp_btn1).click()
    home_Page.login_w_incorrect_credentials(user_info)
    home_Page.wait_for_element_to_appear(home_Page.incorrect_credentials)
    assert driver.find_element(*home_Page.incorrect_credentials).text == "Your email or password is incorrect!"

def test_AE004(browserInstance):
    driver = browserInstance
    home_Page = homePage(driver)
    home_Page.verify_homePage()
    accountInfo_Page = home_Page.register_user(user_info)
    accountInfo_Page.fillUp_infoPage(user_info)
    accountInfo_Page.wait_for_element_to_appear(accountInfo_Page.logout_btn)
    driver.find_element(*accountInfo_Page.logout_btn).click()
    home_Page.wait_for_element_to_appear(home_Page.newUser_txt)
    assert driver.find_element(*home_Page.newUser_txt).text == "New User Signup!"
    home_Page.login_w_correct_credentials(user_info)
    accountInfo_Page.verify_and_delete_account(user_info)

def test_AE005(browserInstance):
    driver = browserInstance
    home_Page = homePage(driver)
    home_Page.verify_homePage()
    accountInfo_Page = home_Page.register_user(user_info)
    accountInfo_Page.fillUp_infoPage(user_info)
    accountInfo_Page.wait_for_element_to_appear(accountInfo_Page.logout_btn)
    driver.find_element(*accountInfo_Page.logout_btn).click()
    home_Page.wait_for_element_to_appear(home_Page.newUser_txt)
    assert driver.find_element(*home_Page.newUser_txt).text == "New User Signup!"
    driver.find_element(*home_Page.signUp_Name_textbox).send_keys(user_info["user_name"])
    driver.find_element(*home_Page.signUp_Email_textbox).send_keys(user_info["email"])
    driver.find_element(*home_Page.signUp_btn2).click()
    home_Page.wait_for_element_to_appear(home_Page.existing_email)
    assert driver.find_element(*home_Page.existing_email).text == "Email Address already exist!"
    home_Page.login_w_correct_credentials(user_info)
    accountInfo_Page.verify_and_delete_account(user_info)


