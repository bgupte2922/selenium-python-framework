import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("Running conftest method level setUp")
    yield
    print("Running conftest method level tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")
    # if browser == 'chrome':
    #     baseUrl = "https://www.letskodeit.com/home"
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #     driver.get(baseUrl)
    #     print("Running tests on chrome")
    # else:
    #     baseUrl = "https://www.letskodeit.com/home"
    #     driver = webdriver.Firefox()
    #     driver.get(baseUrl)
    #     print("Running tests on firefox")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

