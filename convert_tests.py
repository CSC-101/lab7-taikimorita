import unittest
from convert import str_to_float

class TestConvert(unittest.TestCase):
    def test_valid_float(self):
        self.assertEqual(str_to_float("3.14"), 3.14)
        self.assertEqual(str_to_float("0"), 0.0)

    def test_invalid_float(self):
        self.assertIsNone(str_to_float("xyz"))
        self.assertIsNone(str_to_float("3.14.15"))
        self.assertIsNone(str_to_float(""))

if __name__ == '__main__':
    unittest.main()
