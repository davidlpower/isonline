from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class Checker:
   def __init__(self, driver, wait):
      self.driver = driver
      self.wait = wait

   def save_screenshot(self, service_name, item_name):
      file_name = f"{service_name}-{item_name}".replace(" ", "").lower()
      self.driver.save_screenshot(f"screenshots/{file_name}.png")
