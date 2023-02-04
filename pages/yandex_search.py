from pages.yandex_base import BasePage
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search3__button")
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CLASS_NAME, "mini-suggest__item")
    LOCATOR_YANDEX_SEARCH_RESULT = (By.CLASS_NAME, "Link_theme_outer")


class SearchHelper(BasePage):

    def check_search(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def check_suggestions(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_SUGGEST)
        suggestions_items = [x.text for x in all_list if len(x.text) > 0]
        return suggestions_items

    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    def check_search_results(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULT)
        search_results = [x.text for x in all_list if len(x.text) > 0]
        return search_results
