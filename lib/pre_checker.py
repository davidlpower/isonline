from lib.checker import Checker

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

class PreChecker(Checker):
    def __init__(self, driver, wait):  
        super().__init__(driver, wait)

    def run(self, pre_checks):
        try:
            # run each pre check
            for pre_check in pre_checks:
                print(f" > Attempting to complete pre-checks")
                if pre_check['action'] == 'spacebar':
                    self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, pre_check['selector'])))
                    self._spaceBar()
                elif pre_check['action'] == 'click':
                    self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, pre_check['selector'])))
                    self._click(pre_check['selector'])
                else:
                     raise Exception(f"'{pre_check['action']}' is not a valid action")

        except WebDriverException as e:
            print(' - Error: Something went wrong with the pre check')
            print(e)

    # PRIVATE  
    def _spaceBar(self):
        ActionChains(self.driver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

    def _click(self, selector):
        element = self.driver.find_element_by_css_selector(selector)
        element.click()
