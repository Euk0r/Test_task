# Тестовое задание
___
## Оглавление

1. [Описание структуры проекта](#Описание-структуры-проекта)
2. [Используемые библиотеки](#Используемые-библиотеки)
3. [Описание тестовых заданий](#Описание-тестовых-заданий)
   1. [Поиск в яндексе](#Поиск-в-яндексе)
   2. [Картинки на яндексе](#Картинки-на-яндексе)
4. [Запуск тестирования](#Запуск-тестирования)
5. [Логирование и формирование отчета](#Логирование-и-формирование-отчета)
6. [Проблемы](#Проблемы)

___

## Описание структуры проекта

Структура проекта выполнена в соответствии с паттерном программирования **Page Object**.

Test_task/  
├── `conftest.py` - файл для фикстур  
├── `EventListener.py` - файл логгера  
├── `pytest.ini` - инициализация pytest  
├── `requirements.txt` - требуемые библиотеки  
├── pages/ - директория, содержащая реализацию методов для работы со страницей  
│      ├── `__init__.py`  
│      ├── `yandex_base.py`  
│      ├── `yandex_images.py`  
│      └── `yandex_search.py`  
└── tests/ - директория, содержащая реализацию тестов  
        └── `test_yandex.py`  

___

## Используемые библиотеки

В ходе выполнения задания были использованы следующие библиотеки:
```text
selenium
pytest
pytest-html
```

Для установки библиотек используйте комманду:
```commandline
pip install -r requirements.txt
```
___

## Описание тестовых заданий

**Ввиду того, что главная страница яндекса изменилась на Дзен,
было принято решение использовать как стартовую страницу https://ya.ru/.**

**Из-за этого некоторые этапы данных в задании тестов пришлось изменить.**

### Поиск в яндексе

1. Зайти на ya.ru
2. Проверить наличие поля поиска
3. Ввести в поиск Тензор
4. Проверить что появилась таблица с подсказками (suggest)
![ya_search](https://user-images.githubusercontent.com/72356960/216786981-9f9d2d50-31b3-47f6-843e-66472931420b.png)  
5. При нажатии Enter появляется таблица результатов поиска
6. Проверить, что 1 ссылка ведет на сайт tensor.ru

Реализация теста выполнена в методе `test_yandex_search` файла `tests/test_yandex.py`
```python
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
```

Файл `pages/yandex_search.py` содержит реализацию использованных выше методов
для работы с веб элементами страницы

### Картинки на яндексе

1. Зайти на ya.ru
2. Нажать на кнопку всех сервисов
![ya_all_services](https://user-images.githubusercontent.com/72356960/216786963-6fa8a1ca-ba88-4f57-ac70-edf67af12452.png)  
3. Проверить, что ссылка «Картинки» присутствует на странице
![ya_all_services_images](https://user-images.githubusercontent.com/72356960/216786970-003dcb84-6382-4cf3-90a5-eb5f61ee589d.png)  
4. Кликаем на ссылку
5. Проверить, что перешли на url https://yandex.ru/images/
6. Открыть первую категорию
![ya_images_first_category](https://user-images.githubusercontent.com/72356960/216786977-f7d62957-5465-4cc0-a120-1c38009caee6.png)  
7. Проверить, что название категории отображается в поле поиска 
(также проверить совпадение их названий)
![ya_images_category_in_search](https://user-images.githubusercontent.com/72356960/216786976-e0fc3cba-e21b-49fb-ab9b-04d83bd84f0e.png)  
8. Открыть 1 картинку
![ya_images_first_image](https://user-images.githubusercontent.com/72356960/216786979-40c11ece-52d6-4b9b-a854-ce6dfb9b2d5e.png)  
9. Проверить, что картинка открылась
10. Нажать кнопку вперед
![ya_images_forward](https://user-images.githubusercontent.com/72356960/216786980-526d35f0-2a58-46ad-91f2-ebbaa9754daf.png)  
11. Проверить, что картинка сменилась
12. Нажать назад
13. Проверить, что картинка осталась из шага 9 

Реализация теста выполнена в методе `test_yandex_images` файла `tests/test_yandex.py`
```python
def test_yandex_images(browser):
    yandex_main_page = ImageHelper(browser)
    yandex_main_page.go_to_site()
    # there is a bug, when services menu is not displayed
    while yandex_main_page.click_on_the_services_button():
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
```

Файл `pages/yandex_images.py` содержит реализацию использованных выше методов
для работы с веб элементами страницы

___

## Запуск тестирования

Для проведения тестирования необходимо выполнить следующую команду:
```commandline
python -m pytest
```

В результате чего будут выполнены оба теста
___

## Логирование и формирование отчета

Для создания логов работы программы был использован класс `AbstractEventListener`
который позволяет выполнять описанные действия до или после выполнения событий в браузере.

В нашем случае он был использован для написания логов событий.
Для этого был подключен логгер и описаны некоторые методы абстрактного класса.

Для написания логов необходимо применить оболочку `EventFiringWebDriver`, к драйверу:

```python
driver = EventFiringWebDriver(webdriver.Chrome(service=ser, options=op), AnEventListener())
```

Дополнительно в логи добавлялась информация по проведению проверок, выполняемых в тестах.

Пример логов успешного выполнения тестирования:
```text
2023-02-04 20:22:40,961  - INFO - https://ya.ru/ opened
2023-02-04 20:22:40,962  - INFO - Checking for search availability
2023-02-04 20:22:40,962  - INFO - Trying to find "text" by id
2023-02-04 20:22:40,969  - INFO - Trying to find "text" by id
2023-02-04 20:22:40,983  - INFO - Trying to click element with tag "input"
2023-02-04 20:22:41,009  - INFO - Trying to change value of "input"
2023-02-04 20:22:41,040  - INFO - Checking for a table with suggests
2023-02-04 20:22:41,041  - INFO - Trying to find "mini-suggest__item" by class name
2023-02-04 20:22:41,227  - INFO - Trying to find "search3__button" by class name
2023-02-04 20:22:41,242  - INFO - Trying to click element with tag "button"
2023-02-04 20:22:41,265  - INFO - Checking the first link == tensor.ru
2023-02-04 20:22:41,266  - INFO - Trying to find "Link_theme_outer" by class name
2023-02-04 20:22:42,807  - INFO - https://ya.ru/ opened
2023-02-04 20:22:42,808  - INFO - Trying to find "services-pinned__all" by class name
2023-02-04 20:22:42,821  - INFO - Trying to click and redirect to "https://yandex.ru/all"
2023-02-04 20:22:42,864  - INFO - Checking for links to Images
2023-02-04 20:22:42,865  - INFO - Trying to find "services-more-popup__item" by class name
2023-02-04 20:22:43,460  - INFO - Trying to find "[data-statlog='services-more-popup.item.images']" by css selector
2023-02-04 20:22:43,471  - INFO - Trying to click and redirect to "https://yandex.ru/images/"
2023-02-04 20:22:43,509  - INFO - Checking the page link == https://yandex.ru/images/
2023-02-04 20:22:44,227  - INFO - Trying to find "PopularRequestList-SearchText" by class name
2023-02-04 20:22:44,242  - INFO - Trying to find "PopularRequestList-Preview" by class name
2023-02-04 20:22:44,254  - INFO - Trying to click and redirect to "https://yandex.ru/images/search?text=%D0%94%D1%80%D0%B0%D0%B3&nl=1&source=morda"
2023-02-04 20:22:44,285  - INFO - Comparing category names on the main page and in the search
2023-02-04 20:22:44,285  - INFO - Trying to find "input__control" by class name
2023-02-04 20:22:44,300  - INFO - Trying to find "serp-item__link" by class name
2023-02-04 20:22:44,918  - INFO - Trying to click and redirect to "https://yandex.ru/images/search?source=morda&text=%D0%94%D1%80%D0%B0%D0%B3&pos=0&rpt=simage&img_url=http%3A%2F%2Fwallup.net%2Fwp-content%2Fuploads%2F2019%2F09%2F879026-nhra-drag-race-racing-hot-rod-rods.jpg&nl=1&lr=959"
2023-02-04 20:22:45,077  - INFO - Checking for opened image viewer
2023-02-04 20:22:45,078  - INFO - Trying to find "MediaViewer" by class name
2023-02-04 20:22:45,117  - INFO - Trying to find "Link_view_default" by class name
2023-02-04 20:22:45,145  - INFO - Trying to find "CircleButton_type_next" by class name
2023-02-04 20:22:45,188  - INFO - Trying to click element with tag "div"
2023-02-04 20:22:45,240  - INFO - Trying to find "Link_view_default" by class name
2023-02-04 20:22:45,248  - INFO - Comparing first image with second
2023-02-04 20:22:45,249  - INFO - Trying to find "CircleButton_type_prev" by class name
2023-02-04 20:22:45,319  - INFO - Trying to click element with tag "div"
2023-02-04 20:22:45,460  - INFO - Trying to find "Link_view_default" by class name
2023-02-04 20:22:45,494  - INFO - Comparing first image with the opened one
2023-02-04 20:22:45,495  - INFO - Closing driver
```

___

Для формирования отчета была использована библиотека `pytest-html`.
Она позволяет удобно и быстро сформировать полноценный html отчет, готовый к отправке.

Для этого к команде запуска тестирования необходимо добавить параметр `--html=report.html`.
В результате чего сформируется готовый отчет в report.html.

Дополнительно можно использовать параметр `--self-contained-html`, для формирования отчета со встроенными стилями.

Оба этих параметра применяются автоматически при [запуске тестирования](#запуск-тестирования).

Пример отчета: [report-example.html](report-example.html). [Превью](https://htmlpreview.github.io/?https://github.com/Euk0r/Test_task/blob/master/report-example.html).

![report_example](https://user-images.githubusercontent.com/72356960/216786959-40a3e3bb-68e6-4271-aa20-ac366ba95a0d.png)
___

## Проблемы

1. При выполнении [первого теста](#поиск-в-яндексе), после ввода и нажатия кнопки поиска может появиться капча,
которая не позволяет успешно завершить тест, вызывая TimeoutException.  
2. При выполнении [второго теста](#картинки-на-яндексе), в самом начале при открытии страницы может не появиться кнопка
всех сервисов. Было принято решение в случае отсутствия этого меню перезагружать страницу.  
3. Изначально сравнение картинок проверялось по их ссылкам (src).
При таком сравнении, часто возникали моменты, когда одна и та же картинка подгружалась различных размеров.
Из-за чего их ссылки отличались.  
Поэтому было сделано решение проверять картинки по их заголовкам.
Однако возникают случаи, когда первые две картинки имеют одинаковый заголовок,
что не позволяет корректно проверить 11 пункт [второго теста](#картинки-на-яндексе).
