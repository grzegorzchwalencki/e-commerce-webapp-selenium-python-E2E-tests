import sys
sys.path.append(sys.path[0]+"/..")

import unittest
#from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from pages.sign_in_page import Locators
from selenium.webdriver.common.by import By 

class SignInTest(BaseTest):
    """Sign In tests"""
    def setUp(self):
        super().setUp()
        self.sign_in_page = self.home_page.click_sign_in()

# TESTS WITH NO ENTERED CONTENT IN REQUESTED FIELD
    def test_no_email_enter(self):
        """Test sign in with no email entered"""
        # Steps
        # 1. Click Sign In
        # Done in setUp
        # 2. Enter email
        # None 
        # 5. Enter Password
        self.sign_in_page.enter_pass("Testtest!")
        # 7. Click button to create account
        self.sign_in_page.click_sing_in_button()
        
        # EXPECTED RESULT
        # 1. User get an information "This is required field."
        # a) Find all error statements on current webpage
        # b) Check that the number of errors is equal to 1.
        # c) Check if error message is "This is required field"
        self.required_field_error(Locators.EMAIL_ERROR)

    def test_no_lastname_entered(self):
        """Test sign in with no password entered"""
        # Steps
        # 1. Click Sign In
        # Done in setUp
        # 2. Enter email
        self.sign_in_page.enter_email("test@test.pl")
        # 3. Enter Password
        # None
        # 4. Click button to create account
        self.sign_in_page.click_sing_in_button()
        
        # EXPECTED RESULT
        self.required_field_error(Locators.PASSWORD_ERROR)

    def test_wrong_format_email_entered(self):
        """Test sign in with no password entered"""
        # Steps
        # 1. Click Sign In
        # Done in setUp
        # 2. Enter email
        self.sign_in_page.enter_email("test.pl")
        # 3. Enter Password
        self.sign_in_page.enter_pass("Testtest!")
        # 4. Click button to create account
        self.sign_in_page.click_sing_in_button()
        
        # EXPECTED RESULT
        # 1. User get an information "Please enter the same value again."
        expected_msg = "Please enter a valid email address (Ex: johndoe@domain.com)."
        # a) Check if error appear by locator
        user_error_msg = self.driver.find_elements(*Locators.EMAIL_ERROR)
        # b) Check if error message is correct.
        self.assertEqual(expected_msg, user_error_msg[0].text)
    