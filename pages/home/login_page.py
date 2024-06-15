import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[text()='Sign In']"
    _email_field = "//input[@id='email' and @placeholder='Email Address']"
    _password_field = "login-password"
    _login_button = "//button[@id='login']"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.XPATH, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.XPATH, self._login_button)

    # Action performed on the element
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    # Action performed on the element
    def enterEmail(self, email):
        self.clearField(self._email_field, locatorType="xpath")
        self.sendKeys(email, self._email_field, locatorType="xpath")

    # Action performed on the element
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    # Action performed on the element
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    # Functionality that wraps the actions
    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(10)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']/img", "xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("incorrectdetails")
        return result

    def clearFields(self):
        emailField = self.getElement(self._email_field, "xpath")
        emailField.clear()
        passwordField = self.getElement(self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")

    def logout(self):
        self.nav.navigateToUserSettingsIcon()
        logoutLinkElement = self.waitForElement(locator="//a[text()='Logout']", locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)


