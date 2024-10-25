import time
from tabnanny import check

from pageObjects.elements.checkbox_page import CheckBoxPage
from pageObjects.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestCheckbox(BaseClass):

    def test_checkbox(self):

        # Navigate to --> Elements --> Check Box
        home_page = HomePage(self.driver)
        accordion_page = home_page.navigate_to_card('Elements')
        accordion_page.choose_accordion_option("Check Box")

        # Validate page title
        checkbox_page = CheckBoxPage(self.driver)
        assert 'Check Box' == checkbox_page.get_title()

        # Validate text result when all checkboxes marked
        checkbox_page.get_checkbox_by_title('Home').click()
        text_results = checkbox_page.get_results()
        assert ('You have selected : home desktop notes commands documents workspace react angular'
                ' veu office public private classified general downloads wordFile excelFile'
                == text_results)
        checkbox_page.get_checkbox_by_title('Home').click()

        # Collapse tree
        checkbox_page.get_collapse().click()










