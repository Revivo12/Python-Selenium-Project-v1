import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    #driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

