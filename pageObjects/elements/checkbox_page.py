from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckBoxPage:

    def __init__(self, driver):
        self.driver = driver

    title = (By.TAG_NAME, "h1")
    results = (By.ID, "result")
    check_boxes = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    check_boxes_title = (By.CLASS_NAME, 'rct-title')
    expand = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    collapse = (By.CSS_SELECTOR, 'button[title="Collapse all"]')

    def get_title(self):
        return self.driver.find_element(*CheckBoxPage.title).text

    def get_checkboxes(self):
        return self.driver.find_elements(*CheckBoxPage.check_boxes)

    def get_checkboxes_titles(self):
        return self.driver.find_elements(*CheckBoxPage.check_boxes_title)

    def get_results(self):
        text = self.driver.find_element(*CheckBoxPage.results).text
        parsed_text_results = ' '.join(text.split())
        return parsed_text_results

    def get_expand(self):
        return self.driver.find_element(*CheckBoxPage.expand)

    def get_collapse(self):
        return self.driver.find_element(*CheckBoxPage.collapse)

    def get_checkbox_by_title(self, checkbox_title):
        checkboxes = self.driver.find_elements(*CheckBoxPage.check_boxes_title)
        for checkbox in checkboxes:
            if checkbox.text == checkbox_title:
                return checkbox
