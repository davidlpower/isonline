import datetime

from lib.status_checker import StatusChecker
from lib.pre_checker import PreChecker
from lib.config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def initialize():
    config_file = 'services.json'
    configuration = Config(config_file)
    return configuration.services


def printStatus(item, status):
    status = 'Online' if status else "Offline"
    print(f"{item} is '{status}' - {datetime.datetime.now()}")


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
    status_checker = StatusChecker(driver, wait)
    pre_checker = PreChecker(driver, wait)
    services = initialize()

    for service in services:
        # run all defined pre checks
        pre_checker.run(service['pre_checks'])
        # get and save status of each service
        for check in service['checks']['items']:
            status = status_checker.run(check, service['checks']['status'], service)
            # print status of service
            printStatus(f"{service['name']} - {check['name']}", status)

    driver.quit()


if __name__ == '__main__':
    main()
