import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.events import EventFiringWebDriver
from EventListener import AnEventListener


@pytest.fixture(scope="session")
def browser():
    ser = Service(r"C:\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = EventFiringWebDriver(webdriver.Chrome(service=ser, options=op), AnEventListener())
    yield driver
    driver.quit()
