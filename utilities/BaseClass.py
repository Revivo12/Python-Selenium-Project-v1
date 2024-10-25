import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def wait_for_element_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def force_click(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)
