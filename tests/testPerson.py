import unittest
from lib.check import Check


class TestCheck(unittest.TestCase):

    def test_can_init_check(self):
        name = 'check_name'
        uri = 'check_uri'

        check_under_test = Check(name, uri)
        self.assertEqual(check_under_test.name, name,
                         f"name {name} not found in check")

        self.assertEqual(check_under_test.uri, uri,
                         f"uri {uri} not found in check")
