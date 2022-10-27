import unittest
import baseconverter

class BVA(unittest.TestCase):
    def test_allc_somep(self):
        n = 3
        b = 8
        self.assertEqual(baseconverter.convert_number(n,b), '3')
        n = 22
        b = 12
        self.assertEqual(baseconverter.convert_number(n,b), '1A')
        n = 11
        b = 12
        self.assertEqual(baseconverter.convert_number(n,b), 'B')

if __name__ == '__main__':
    unittest.main(verbosity=2)
