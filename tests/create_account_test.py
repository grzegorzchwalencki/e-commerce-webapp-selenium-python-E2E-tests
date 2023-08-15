import sys
sys.path.append(sys.path[0]+"/..")

import unittest
#from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from pages.create_account_page import Locators
from selenium.webdriver.common.by import By 


class CreateAccountTest(BaseTest):
    """Create Account tests"""
    def setUp(self):
        super().setUp()
        self.create_account_page = self.home_page.click_create_account()
    
# TESTS WITH NO ENTERED CONTENT IN REQUESTED FIELD
    def test_no_firstname_enter(self):
        """Test create account with no first name entered"""
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        # not
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter email
        self.create_account_page.enter_email("test@test.pl")
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        # 1. User get an information "This is required field."
        # a) Find all error statements on current webpage
        # b) Check that the number of errors is equal to 1.
        # c) Check if error message is "This is required field"
        self.required_field_error(Locators.FIRST_NAME_ERROR)

    def test_no_lastname_entered(self):
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        # Non
        # 4. Enter email
        self.create_account_page.enter_email("test@test.pl")
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        self.required_field_error(Locators.LAST_NAME_ERROR)

    def test_no_email_entered(self):
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter email
        # None
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        self.required_field_error(Locators.EMAIL_ERROR)

    def test_no_password_entered(self):
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter email
        self.create_account_page.enter_email("test@test.pl")
        # 5. Enter Password
        # None
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        self.required_field_error(Locators.PASSWORD_ERROR)

    def test_no_password_confirmation_entered(self):
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter email
        self.create_account_page.enter_email("test@test.pl")
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        # None
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        self.required_field_error(Locators.PASSWORD_CONF_ERROR)

    def test_wrong_email_format(self):
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter wrong format of email
        self.create_account_page.enter_email("testpl")
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
    
        # EXPECTED RESULT
        # 1. User get an information "Please enter a valid email address (Ex: johndoe@domain.com)."
        # a) Check if error appear by locator
        user_error_msg = self.driver.find_elements(*Locators.EMAIL_ERROR)
        # b) Check if error message is correct.
        self.assertEqual("Please enter a valid email address (Ex: johndoe@domain.com).", user_error_msg[0].text)

    def test_too_short_password_entered(self):
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter wrong format of email
        self.create_account_page.enter_email("testpl")
        # 5. Enter Password
        self.create_account_page.enter_password("12345")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("12345")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
    
        # EXPECTED RESULT
        # 1. User get an information "Minimum length of this field must be equal or 
        # greater than 8 symbols. Leading and trailing spaces will be ignored."
        expected_msg = "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored."
        # a) Check if error appear by locator
        user_error_msg = self.driver.find_elements(*Locators.PASSWORD_ERROR)
        # b) Check if error message is correct.
        self.assertEqual(expected_msg, user_error_msg[0].text)

    def test_con_passwd_notequal_to_passwd(self):
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter wrong format of email
        self.create_account_page.enter_email("testpl")
        # 5. Enter Password
        self.create_account_page.enter_password("TestTest1")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("TestTest2")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
    
        # EXPECTED RESULT
        # 1. User get an information "Please enter the same value again."
        expected_msg = "Please enter the same value again."
        # a) Check if error appear by locator
        user_error_msg = self.driver.find_elements(*Locators.PASSWORD_CONF_ERROR)
        # b) Check if error message is correct.
        self.assertEqual(expected_msg, user_error_msg[0].text)