import unittest
from length import *

class TestLength(unittest.TestCase):

    def setUp(self):
        pass

    def test_unit_has_short_name_as_string_rep(self):
        self.assertEqual(str(YARD), 'yd')
        self.assertEqual(str(METRE), 'm')
        self.assertEqual(str(INCH), 'in')

    def test_unit_can_convert_to_mm(self):
        self.assertEqual(YARD.to_mm(3), 3 * 9140)
        self.assertEqual(METRE.to_mm(0.5), 500)
        self.assertEqual(INCH.to_mm(20), 20 * 254)

    def test_unit_can_convert_from_mm(self):
        self.assertEqual(YARD.from_mm(0.7 * 9140), 0.7)
        self.assertEqual(METRE.from_mm(6800), 6.8)
        self.assertEqual(INCH.from_mm(508), 2.0)

    def test_lengths_have_user_friendly_string_rep(self):
        self.assertEqual(str(Length(2.3, YARD)), '2.30 yd')
        self.assertEqual(str(Length(0.3, METRE)), '0.30 m')
        self.assertEqual(str(Length(38, INCH)), '38.00 in')

if __name__ == '__main__':
    unittest.main()
