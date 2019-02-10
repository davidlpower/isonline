import unittest
from lib.config import Config


class TestCheck(unittest.TestCase):

    def test_can_init_check(self):
        # Arrange
        service_name = 'service_name'
        service_url = 'service_url'
        no_of_status = 2
        check_name = 'service_check_name'
        check_uri = 'service_check_uri'

        # Act
        config_under_test = Config('tests/fixtures/test_services.json')
        services = config_under_test.services[0]

        # Assert
        self.assertEqual(services['name'], service_name)
        self.assertEqual(services['url'], service_url)
        self.assertEqual(len(services['status']), no_of_status)
        self.assertEqual(len(services['checks']), 1)
        self.assertEqual(services['checks'][0]['name'], check_name)
        self.assertEqual(services['checks'][0]['uri'], check_uri)
