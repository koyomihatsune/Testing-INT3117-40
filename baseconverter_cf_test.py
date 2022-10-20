import unittest
import baseconverter

class BVA(unittest.TestCase):
    def test_control_flow_c2(self):
        n = -2
        b = 8
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid')
        n = 0
        b = 8
        self.assertEqual(baseconverter.convert_number(n,b), '0')
        n = 50
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), '110010')
        n = 9023
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), '233F')

if __name__ == '__main__':
    unittest.main(verbosity=2)
