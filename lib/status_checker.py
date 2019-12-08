from lib.checker import Checker

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class StatusChecker(Checker):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def run(self, item, status, service):
        try:
            self.wait.until(
                expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, status['selector']),status['indicator']))
            return True
        except WebDriverException:
            self.save_screenshot(service['name'], item['name'])
            return False
