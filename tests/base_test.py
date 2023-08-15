import sys
sys.path.append(sys.path[0]+"/..")

from selenium import webdriver
import unittest
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """Base class to use in every test"""
    def setUp(self):
        """ Initial conditions in every test"""
        # Open browser
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.home_page = HomePage(self.driver)

    def required_field_error(self, field_error_locator):
        """ Method to check if expected error message 
        "This field is required." is appeared"""
        # a) Find all error statements on current webpage
        user_error_msg = self.driver.find_elements(*field_error_locator)
        # b) Check that the number of errors is equal to 1.
        self.assertEqual(1, len(user_error_msg))
        # c) Check if error message is "This is required field"
        self.assertEqual("This is a required field.", user_error_msg[0].text)

    def tearDown(self):
        self.driver.quit()

