import unittest
import length

class TestLength(unittest.TestCase):

    def setUp(self):
        pass

    def test_unit_has_short_name_as_string_rep(self):
        self.assertEqual(str(length.YARD), 'yd')
        self.assertEqual(str(length.METRE), 'm')
        self.assertEqual(str(length.INCH), 'in')

if __name__ == '__main__':
    unittest.main()
