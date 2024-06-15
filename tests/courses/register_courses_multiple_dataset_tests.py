from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from base.selenium_driver import SeleniumDriver

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesMultipleDatasetTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234123412341234"), ("Selenium WebDriver 4 With Python", "7894789478947894"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum):
        self.courses.clickAllCourseLink()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Invalid enrollment verification")
        assert result == True
        # self.driver.find_element_by_link_text("ALL COURSES").click()












