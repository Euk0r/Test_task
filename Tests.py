from pages.YandexSearch import SearchHelper
from pages.YandexImages import ImageHelper


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    assert yandex_main_page.check_search()
    yandex_main_page.enter_word("Тензор")
    assert yandex_main_page.check_suggestions()
    yandex_main_page.click_on_the_search_button()
    elements = yandex_main_page.check_search_results()
    assert "tensor.ru" == elements[0]


def test_yandex_images(browser):
    yandex_main_page = ImageHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_on_the_services_button()
    elements = yandex_main_page.check_services()
    assert "Картинки" in elements
    yandex_main_page.click_on_the_images_service()
    yandex_main_page.switch_window(1)
    assert yandex_main_page.get_url() == "https://yandex.ru/images/"
    category_name = yandex_main_page.get_name_of_the_first_category()
    yandex_main_page.click_on_the_first_image_category()
    assert yandex_main_page.check_category_in_search() == category_name
    yandex_main_page.click_on_the_first_image()
    assert yandex_main_page.check_image_opened()
    first_image = yandex_main_page.get_current_image_title()
    yandex_main_page.click_on_the_next_image()
    second_image = yandex_main_page.get_current_image_title()
    assert first_image != second_image
    yandex_main_page.click_on_the_prev_image()
    changed_image = yandex_main_page.get_current_image_title()
    assert changed_image == first_image
