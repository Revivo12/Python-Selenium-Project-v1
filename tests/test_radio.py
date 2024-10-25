import time
from re import match

from BaseClass import BaseClass
from elements.radiobutton_page import RadioButtonPage
from home_page import HomePage


class TestRadioButtons(BaseClass):

    def test_radio_buttons(self):

        # Navigate to --> Elements --> Radio Button
        home_page = HomePage(self.driver)
        accordion_page = home_page.navigate_to_card('Elements')
        accordion_page.choose_accordion_option('Radio Button')

        # Assert page title = Radio Button
        radio_button_page = RadioButtonPage(self.driver)
        self.wait_for_element_visibility(radio_button_page.yes)
        assert 'Radio Button' == radio_button_page.get_title()

        # Validate "Yes" radio button is enabled
        assert not radio_button_page.get_radio_button_yes().is_selected()
        self.force_click(radio_button_page.get_radio_button_yes())
        assert radio_button_page.get_radio_button_yes().is_selected()
        assert 'You have selected Yes' in radio_button_page.get_text_results()

        # Validate "Impressive" radio button is enabled
        assert not radio_button_page.get_radio_button_impressive().is_selected()
        self.force_click(radio_button_page.get_radio_button_impressive())
        assert radio_button_page.get_radio_button_impressive().is_selected()
        assert 'You have selected Impressive' in radio_button_page.get_text_results()

        # Validate "No" radio button is not enabled
        assert not radio_button_page.get_radio_button_no().is_enabled()


