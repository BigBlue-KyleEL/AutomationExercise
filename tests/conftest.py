import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(service=FirefoxService(), options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=EdgeService(), options=options)
    else:
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    driver.maximize_window()
    driver.get("https://automationexercise.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
