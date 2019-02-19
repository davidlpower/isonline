from lib.status_checker import StatusChecker
from lib.factories.status_check_item_factory import StatusCheckItemFactory
from lib.config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def initialize():
    config_file = 'services.json'
    stauts_check_items = []
    item_factory = StatusCheckItemFactory()
    configuration = Config(config_file)

    for service in configuration.services:
        for check in service['checks']:
            stauts_check_items.append(item_factory.build(service, check))
    return stauts_check_items


def printStatus(item, status):
    status = 'Online' if status else "Offline"
    print(f"{item.id} is '{status}'.")


def createDriver():
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                              desired_capabilities={
                                  'browserName': 'chrome',
                                  'javascriptEnabled': True
                              })
    wait = WebDriverWait(driver, 10)
    return driver, wait


def main():
    driver, wait = createDriver()
    checker = StatusChecker(driver, wait)
    status_check_items = initialize()

    for item in status_check_items:
        status = checker.get_status(item)
        printStatus(item, status)

    driver.quit()


if __name__ == '__main__':
    main()
