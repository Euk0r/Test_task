from pages.yandex_search import SearchHelper
from pages.yandex_images import ImageHelper
from EventListener import logger


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    logger.info("Checking for search availability")
    assert yandex_main_page.check_search()
    yandex_main_page.enter_word("Тензор")
    logger.info("Checking for a table with suggests")
    assert yandex_main_page.check_suggestions()
    yandex_main_page.click_on_the_search_button()
    logger.info("Checking the first link == tensor.ru")
    elements = yandex_main_page.check_search_results()
    assert "tensor.ru" == elements[0]


def test_yandex_images(browser):
    yandex_main_page = ImageHelper(browser)
    yandex_main_page.go_to_site()
    while yandex_main_page.click_on_the_services_button():  # there is a bug, when services menu is not displayed
        yandex_main_page.refresh_page()
    logger.info("Checking for links to Images")
    elements = yandex_main_page.check_services()
    assert "Картинки" in elements
    yandex_main_page.click_on_the_images_service()
    yandex_main_page.switch_window(1)
    logger.info("Checking the page link == https://yandex.ru/images/")
    assert yandex_main_page.get_url() == "https://yandex.ru/images/"
    category_name = yandex_main_page.get_name_of_the_first_category()
    yandex_main_page.click_on_the_first_image_category()
    logger.info("Comparing category names on the main page and in the search")
    assert yandex_main_page.check_category_in_search() == category_name
    yandex_main_page.click_on_the_first_image()
    logger.info("Checking for opened image viewer")
    assert yandex_main_page.check_image_opened()
    first_image = yandex_main_page.get_current_image_title()
    yandex_main_page.click_on_the_next_image()
    second_image = yandex_main_page.get_current_image_title()
    logger.info("Comparing first image with second")
    assert first_image != second_image
    yandex_main_page.click_on_the_prev_image()
    changed_image = yandex_main_page.get_current_image_title()
    logger.info("Comparing first image with the opened one")
    assert changed_image == first_image

# to run: python -m pytest
