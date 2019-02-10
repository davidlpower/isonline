import unittest
from lib.service import Service


class TestService(unittest.TestCase):

    def test_can_init_service(self):
        # Arrange
        name = 'service_name'
        url = 'service_url'
        status = 'service_status'

        # Act
        service_under_test = Service(name, url, status)

        # Assert
        self.assertEqual(service_under_test.name, name,
                         f"name {name} not found in Service")

        self.assertEqual(service_under_test.url, url,
                         f"uri {url} not found in Service")

        self.assertEqual(service_under_test.status, status,
                         f"uri {status} not found in Service")
