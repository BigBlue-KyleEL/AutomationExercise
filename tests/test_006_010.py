from page_Objects.homePage import homePage


contact_info = {
    "name": "Clark Kent",
    "email": "clark@dailyplanet.com",
    "subject": "test",
    "message": "test",
    "file_path": "../utilities/Empty.txt",
    "file_name": "Empty.txt"
}

def test_AE006(browserInstance):
    driver = browserInstance
    home_Page = homePage(driver)
    home_Page.verify_homePage()
    home_Page.contact_us(contact_info)

def test_AE007(browserInstance):
    driver = browserInstance
    home_Page = homePage(driver)
    home_Page.verify_homePage()
    home_Page.verify_TestCases_page()

# def test_AE008(browserInstance):
#     driver = browserInstance
#     home_Page = homePage(driver)
#     home_Page.verify_homePage()


