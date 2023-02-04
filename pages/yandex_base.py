from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def find_element(self, locator, time=10):
        self.driver.implicitly_wait(3)
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        self.driver.implicitly_wait(3)
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def switch_window(self, id_window):
        return self.driver.switch_to.window(self.driver.window_handles[id_window])

    def refresh_page(self):
        self.driver.implicitly_wait(5)
        return self.driver.refresh()
