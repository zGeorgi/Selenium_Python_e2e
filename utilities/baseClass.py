import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import logging
import inspect




@pytest.mark.usefixtures("invoke_browser")
class BaseClass:

    def getLog_obj(self):
        test_name = inspect.stack()[1][3]
        logging.getLogger(test_name).handlers.clear()
        log = logging.getLogger(test_name)

        file_h = logging.FileHandler("/home/georgi/PycharmProjects/E_Shop/utilities/logfile.log")
        formatter = logging.Formatter("%(asctime)s => %(levelname)s => %(name)s => %(message)s")
        file_h.setFormatter(formatter)
        log.addHandler(file_h)
        log.setLevel(logging.DEBUG)
        return log

    def wait_link_presence(self, text, seconds):
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, text)))

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
