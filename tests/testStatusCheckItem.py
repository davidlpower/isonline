import unittest
from lib.status_check_item import StatusCheckItem
from lib.service import Service
from lib.check import Check


"""
class StatusCheckItem:
    def __init__(self, service, check):
        self.id = f"{service.name} - {check.name}"
        self.url = f"{service.url}{check.uri}"
        self.selector = service.status['selector']
        self.indicator = service.status['indicator']

"""


class TestStatusCheckItem(unittest.TestCase):

    def test_can_init_statuscheckitem(self):
        # Arrange
        service_name = 'service_name'
        service_url = 'service_url'
        service_status = {
            'selector': 'test_selector',
            'indicator': 'test_indicator'
            }
        check_name = 'service_check_name'
        check_uri = 'service_check_uri'

        # Arrange - expected
        expected_id = f"{service_name} - {check_name}"
        expected_url = f"{service_url}{check_uri}"
        expected_selector = service_status['selector']
        expected_indicator = service_status['indicator']

        test_service = Service(service_name, service_url, service_status)
        test_check = Check(check_name, check_uri)

        # Act
        status_check_item_under_test = StatusCheckItem(test_service,
                                                       test_check)

        # Assert
        self.assertEqual(status_check_item_under_test.id, expected_id)
        self.assertEqual(status_check_item_under_test.url, expected_url)
        self.assertEqual(status_check_item_under_test.selector,
                         expected_selector)
        self.assertEqual(status_check_item_under_test.indicator,
                         expected_indicator)
