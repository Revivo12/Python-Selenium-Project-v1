from selenium.webdriver.common.by import By

class AccordionPage:

    def __init__(self, driver):
        self.driver = driver

    accordion_content = (By.CSS_SELECTOR, '.element-list.show')
    accordion_options = (By.CSS_SELECTOR, '.element-list.show .menu-list li')

    def get_shown_accordion(self):
        return self.driver.find_elements(*AccordionPage.accordion_options)

    def choose_accordion_option(self, accordion_option):
        options = self.get_shown_accordion()
        for option in options:
            if option.text == accordion_option:
                option.click()


