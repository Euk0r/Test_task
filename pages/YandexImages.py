from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexImagesLocators:
    LOCATOR_YANDEX_SEARCH_SERVICES_LIST = (By.CLASS_NAME, "services-pinned__all")
    LOCATOR_YANDEX_SEARCH_SERVICES_ITEM = (By.CLASS_NAME, "services-more-popup__item")
    LOCATOR_YANDEX_SEARCH_SERVICE_IMAGES = (By.CSS_SELECTOR, "[data-statlog='services-more-popup.item.images']")
    LOCATOR_YANDEX_IMAGE_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Preview")
    LOCATOR_YANDEX_IMAGE_CATEGORY_NAME = (By.CLASS_NAME, "PopularRequestList-SearchText")
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CLASS_NAME, "input__control")
    LOCATOR_YANDEX_IMAGE_ITEM = (By.CLASS_NAME, "serp-item__link")
    LOCATOR_YANDEX_IMAGE_VIEWER = (By.CLASS_NAME, "MediaViewer")
    LOCATOR_YANDEX_IMAGE_VIEWER_LINK = (By.CLASS_NAME, "Link_view_default")
    LOCATOR_YANDEX_IMAGE_VIEWER_NEXT = (By.CLASS_NAME, "CircleButton_type_next")
    LOCATOR_YANDEX_IMAGE_VIEWER_PREV = (By.CLASS_NAME, "CircleButton_type_prev")


class ImageHelper(BasePage):

    def click_on_the_services_button(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_SEARCH_SERVICES_LIST).click()

    def check_services(self):
        all_list = self.find_elements(YandexImagesLocators.LOCATOR_YANDEX_SEARCH_SERVICES_ITEM)
        available_services = [x.text for x in all_list if len(x.text) > 0]
        return available_services

    def click_on_the_images_service(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_SEARCH_SERVICE_IMAGES).click()

    def get_name_of_the_first_category(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGE_CATEGORY_NAME).get_attribute("innerHTML")

    def click_on_the_first_image_category(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGE_CATEGORY).click()

    def check_category_in_search(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_SEARCH_FIELD).get_attribute("value")

    def click_on_the_first_image(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGE_ITEM).click()

    def check_image_opened(self):
        return self.find_elements(YandexImagesLocators.LOCATOR_YANDEX_IMAGE_VIEWER)

    def get_current_image_title(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGE_VIEWER_LINK).get_attribute("innerHTML")

    def click_on_the_next_image(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGE_VIEWER_NEXT).click()

    def click_on_the_prev_image(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGE_VIEWER_PREV).click()
