import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "//a[text()='MY COURSES']"
    _all_courses = "ALL COURSES"
    _practice = "//a[contains(text(),'PRACTICE')]"
    _element_practice = "//a[text()='Element Practice']"
    _user_settings_icon = "//button[@id='dropdownMenu1']/img"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="linktext")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="xpath")

    def navigateToElementPractice(self):
        self.elementClick(locator=self._element_practice, locatorType="xpath")

    def navigateToUserSettingsIcon(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)
