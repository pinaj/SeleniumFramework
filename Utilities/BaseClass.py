import inspect
import logging

import FileHandler
import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")

class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def select_option_text(self,locator,text):
        dropdown_values = Select(locator)
        dropdown_values.select_by_visible_text(text)