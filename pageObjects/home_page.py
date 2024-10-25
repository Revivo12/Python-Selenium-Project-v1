from selenium.webdriver.common.by import By
from pageObjects.accordion_page import AccordionPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    cards_titles = (By.CLASS_NAME, "card-body")

    def get_cards_titles(self):
        return self.driver.find_elements(*HomePage.cards_titles)

    def navigate_to_card(self, card_name):
        cards_titles = self.get_cards_titles()
        for card in cards_titles:
            if card.text == card_name:
                card.click()
                return AccordionPage(self.driver)

