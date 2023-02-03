import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from EventListener import AnEventListener


@pytest.fixture(scope="session")
def browser():
    driver = EventFiringWebDriver(webdriver.Chrome(executable_path="./chromedriver"), AnEventListener())
    yield driver
    driver.quit()
