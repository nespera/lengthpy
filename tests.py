import unittest
from length import *

class TestLengthUnit(unittest.TestCase):

    def setUp(self):
        pass

    def test_unit_has_short_name_as_string_rep(self):
        self.assertEqual(str(YARD), 'yd')
        self.assertEqual(str(METRE), 'm')
        self.assertEqual(str(INCH), 'in')

    def test_unit_can_convert_to_mm(self):
        self.assertEqual(YARD.to_mm(3), 3 * 914)
        self.assertEqual(METRE.to_mm(0.5), 500)
        self.assertEqual(INCH.to_mm(20), 20 * 254)

    def test_unit_can_convert_from_mm(self):
        self.assertEqual(YARD.from_mm(0.7 * 914), 0.7)
        self.assertEqual(METRE.from_mm(6800), 6.8)
        self.assertEqual(INCH.from_mm(508), 2.0)

class TestLength(unittest.TestCase):

    def test_lengths_have_user_friendly_string_rep(self):
        self.assertEqual(str(Length(2.3, YARD)), '2.30 yd')
        self.assertEqual(str(Length(0.3, METRE)), '0.30 m')
        self.assertEqual(str(Length(38, INCH)), '38.00 in')

    def test_conversion(self):
        in_metres = Length(2.3, YARD).convert_to(METRE)
        self.assertEqual(in_metres.unit, METRE)
        self.assertAlmostEqual(in_metres.magnitude, 2.1022)
        self.assertEqual(str(in_metres), '2.10 m')

if __name__ == '__main__':
    unittest.main()
