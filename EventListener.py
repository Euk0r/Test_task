import logging
from selenium.webdriver.support.events import AbstractEventListener

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)

f_handler = logging.FileHandler('./report.log')
formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

f_handler.setFormatter(formatter)
logger.addHandler(f_handler)


class AnEventListener(AbstractEventListener):
    logger = logger

    def after_navigate_to(self, url, driver):
        logger.info("%s opened" % url)

    def before_find(self, by, value, driver):
        logger.info("Trying to find \"%s\" by %s" % (value, by))

    # using "before" instead of "after" because of StaleElementReferenceException
    def before_click(self, element, driver):
        link = element.get_attribute("href")
        if link:
            logger.info("Trying to click and redirect to \"%s\"" % link)
        else:
            logger.info("Trying to click element with tag \"%s\"" % element.tag_name)

    def before_change_value_of(self, element, driver):
        logger.info("Trying to change value of \"%s\"" % element.tag_name)

    def before_quit(self, driver):
        logger.info("Closing driver")

    def on_exception(self, exception, driver):
        logger.exception(exception)
