from selenium import webdriver
from pages.base_page import BasePage
from pages.sign_in_page import SignInPage
from pages.create_account_page import CreateAccountPage
from selenium.webdriver.common.by import By

class Locators:
    """Locators on Home Page"""
    SIGN_IN_LINK = (By.PARTIAL_LINK_TEXT, "Sign In")
    CREATE_ACCOUNT_LINK = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/customer/account/create/"]')
    WHATS_NEW_PAGE = (By.ID, "ui-id-3")
    WOMEN_PAGE = (By.ID, "ui-id-4")
    MAN_PAGE = (By.ID, "ui-id-5")
    GEAR_PAGE = (By.ID, "ui-id-6")
    TRAINING_PAGE = (By.ID, "ui-id-7")
    SALE_PAGE = (By.ID, "ui-id-8")

class HomePage(BasePage):
    """Main Page"""
    
    def click_sign_in(self):
        """Click link to sing in page"""
        #1. Find element - (sign in)
        el_sign_in = self.driver.find_element(*Locators.SIGN_IN_LINK)
        #2. Click sing in button
        el_sign_in.click()
        #3. Return log in page
        return SignInPage(self.driver)
    
    def click_create_account(self):
        """Click link to create account page"""
        #1. Find element - (create account)
        el_crea_acc = self.driver.find_element(*Locators.CREATE_ACCOUNT_LINK)
        #2. Click 
        el_crea_acc.click()
        #3. Return log in page
        return CreateAccountPage(self.driver)
    

    