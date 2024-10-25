from selenium.webdriver.common.by import By


class RadioButtonPage:

    def __init__(self, driver):
        self.driver = driver


    title = (By.TAG_NAME, 'h1')
    yes = (By.ID, 'yesRadio')
    no = (By.ID, 'noRadio')
    impressive = (By.ID, 'impressiveRadio')
    textResults = (By.CSS_SELECTOR, 'p[class="mt-3"]')

    def get_title(self):
        return self.driver.find_element(*RadioButtonPage.title).text

    def get_radio_button_yes(self):
        return self.driver.find_element(*RadioButtonPage.yes)

    def get_radio_button_no(self):
        return self.driver.find_element(*RadioButtonPage.no)

    def get_radio_button_impressive(self):
        return self.driver.find_element(*RadioButtonPage.impressive)

    def get_text_results(self):
        return self.driver.find_element(*RadioButtonPage.textResults).text

