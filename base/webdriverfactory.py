"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
        wdf = WebDriverFactory(browser)
        wdf.getWebDriverInstance()
"""

import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        :returns
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine where browser will be executed
    """
    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        :return: WebDriver Instance
        """
        baseUrl = "https://www.letskodeit.com/home"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        # Setting Driver Implicit Time Out for An Element
        driver.implicitly_wait(10)
        # Maximize window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseUrl)
        return driver


