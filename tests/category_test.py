import sys
sys.path.append(sys.path[0]+"/..")

from tests.base_test import BaseTest
from pages.category_pages import Locators
from selenium.webdriver.common.by import By 

class WomenCategoryTest(BaseTest):
    """Category tests"""
    def setUp(self):
        super().setUp()
        self.category_page = self.home_page.click_women_page()    

    def test_open_tops_category(self):
        """Test OPEN"""
        self.category_page.open_tops_category()
        
        #self.category_page.change_item_amount_on_page()
        # Steps
        # 1. Click Sign In
        # Done in setUp
        # 2. 
        # None 
        # 5. Enter Password
        
   
    