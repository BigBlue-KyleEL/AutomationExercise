import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")

    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)
    else:
        driver = webdriver.Chrome(service=service_obj)

    driver.maximize_window()
    driver.get("https://automationexercise.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.close()
