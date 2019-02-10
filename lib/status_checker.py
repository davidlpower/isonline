from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains


class StatusChecker:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def accept_mature_warning(self):
        ActionChains(self.driver).key_down(
            Keys.ENTER).key_up(Keys.ENTER).perform()

    def get_status(self, check_item):
        self.driver.get(check_item.url)
        try:
            self.accept_mature_warning()
            self.wait.until(
                expected_conditions.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, check_item.selector),
                    check_item.indicator))
            return True
        except WebDriverException:
            file_name = check_item.id.replace(" ", "").lower()
            self.driver.save_screenshot(f"{file_name}.png")
            return False
