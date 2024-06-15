import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _all_courses = "ALL COURSES" # link text
    _search_box = "//input[@id='search']"
    # _course = "//div[@id='course-list']//h4[contains(text(),'{0}')]"
    _course = "//h4[@class='dynamic-heading' and contains(text(),'{0}')]"
    _enroll_button = "//button[text()='Enroll in Course']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date" # name
    _cc_cvv = "//input[@name='cvc']"
    _submit_enroll = "//div[@class='col-xs-12']//button[contains(@class,'sp-buy')]"
    _enroll_error_message = "//div[@class='cc-payment-outer']//li/span"
    _card_list = "__PrivateStripeElement-input"
    _search_button = "//button[@type='submit']"

    def clickAllCourseLink(self):
        self.elementClick(self._all_courses, "linktext")

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, "xpath")
        self.elementClick(self._search_button, "xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(fullCourseName, self._course, "xpath")

    def enterCardNum(self, num):
        time.sleep(10)
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()
        time.sleep(5)
        self.webScroll(direction="up")


    # def enterCardExp(self, exp):
    #     self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
    #     self.sendKeysWhenReady(exp, locator=self._cc_exp, locatorType="name")
    #     self.switchToDefaultContent()

    # def enterCardCVV(self, cvv):
    #     self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
    #     self.sendKeysWhenReady(cvv, locator=self._cc_cvv, locatorType="xpath")
    #     self.switchToDefaultContent()

    # def clickEnrollSubmitButton(self):
    #     self.elementClick(self._submit_enroll, "xpath")

    def enterCreditCardInformation(self, num):
        self.enterCardNum(num)
        # self.enterCardExp(exp)
        # self.enterCardCVV(cvv)

    def enrollCourse(self, num):
        # Click on the enroll button
        self.elementClick(self._enroll_button, "xpath")
        # Scroll down
        self.webScroll(direction="down")
        # Enter credit card information
        self.enterCreditCardInformation(num)
        # Click enroll in course button
        # self.clickEnrollSubmitButton()
        time.sleep(2)

    def verifyEnrollFailed(self):
        # result = self.isElementDisplayed(self._enroll_error_message, "xpath")
        # if result is False:
        #     result = self.waitForElement(self._enroll_error_message, "xpath")
        # else:
        #     return result
        # self.waitForElement(self._enroll_error_message, "xpath")
        result = self.isElementDisplayed(self._enroll_error_message, "xpath") # to FAIL test case, change xpath to name
        if result is True:
            return result
        else:
            return False

    def verifyCourse(self):
        return self.verifyPageTitle("My Courses")













