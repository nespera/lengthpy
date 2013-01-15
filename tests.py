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
        self.assertEqual(str(Length(0.3, METRE)), '0.30 m')
        self.assertEqual(str(Length(38, INCH)), '38.00 in')

if __name__ == '__main__':
    unittest.main()
