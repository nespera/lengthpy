import unittest
from length import *

class TestLength(unittest.TestCase):

    def setUp(self):
        pass

    def test_unit_has_short_name_as_string_rep(self):
        self.assertEqual(str(YARD), 'yd')
        self.assertEqual(str(METRE), 'm')
        self.assertEqual(str(INCH), 'in')

    def test_lengths_have_user_friendly_string_rep(self):
        self.assertEqual(str(Length(2.3, YARD)), '2.30 yd')

if __name__ == '__main__':
    unittest.main()
