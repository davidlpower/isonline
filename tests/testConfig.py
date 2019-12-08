import unittest
from lib.config import Config


class TestConfig(unittest.TestCase):

    def test_can_init_config(self):
        # Arrange
        service_name = 'service_name'
        service_url = 'https://www.service_url.com'
        no_of_checks = 1
        check_name = 'Person'
        check_uri = '/person'
        pre_check_selector = 'pre_checks_selector'
        pre_check_action = 'click'
        
        # Act
        config_under_test = Config('tests/fixtures/test_services.json')
        services = config_under_test.services[0]

        # Assert
        self.assertEqual(services['name'], service_name)
        self.assertEqual(services['url'], service_url)
        self.assertEqual(len(services['checks']['items']), no_of_checks)
        self.assertEqual(services['checks']['items'][0]['name'], check_name)
        self.assertEqual(services['checks']['items'][0]['uri'], check_uri)
        self.assertEqual(services['pre_checks'][0]['action'], pre_check_action)
        self.assertEqual(services['pre_checks'][0]['selector'], pre_check_selector)
