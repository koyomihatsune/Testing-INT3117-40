import unittest
import baseconverter

class BVA(unittest.TestCase):
    def test_boundary_strong(self):
        n = -1
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')
        n = 0
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '0')
        n = 1
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '1')
        n = 500000
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '4151504')
        n = 999999
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '11333310')
        n = 1000000
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '11333311')
        n = 1000001
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')
        n = 500000
        b = 1
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 500000
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), '1111010000100100000')
        n = 500000
        b = 3
        self.assertEqual(baseconverter.convert_number(n,b), '221101212112')
        n = 500000
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '4151504')
        n = 500000
        b = 15
        self.assertEqual(baseconverter.convert_number(n,b), '9D235')
        n = 500000
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), '7A120')
        n = 500000
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = -1
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number and base')

    def test_boundary_combined(self):
        n = -1
        b = 1
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number and base')
        n = 0
        b = 1
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 1
        b = 1
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 500000
        b = 1
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 999999
        b = 1
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 1000000
        b = 1
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 1000001
        b = 1
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number and base')

        n = -1
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')
        n = 0
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), '0')
        n = 1
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), '1')
        n = 500000
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), '1111010000100100000')
        n = 999999
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), '11110100001000111111')
        n = 1000000
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), '11110100001001000000')
        n = 1000001
        b = 2
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')

        n = -1
        b = 3
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')
        n = 0
        b = 3
        self.assertEqual(baseconverter.convert_number(n,b), '0')
        n = 1
        b = 3
        self.assertEqual(baseconverter.convert_number(n,b), '1')
        n = 500000
        b = 3
        self.assertEqual(baseconverter.convert_number(n,b), '221101212112')
        n = 999999
        b = 3
        self.assertEqual(baseconverter.convert_number(n,b), '1212210202000')
        n = 1000000
        b = 3
        self.assertEqual(baseconverter.convert_number(n,b), '1212210202001')
        n = 1000001
        b = 3
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')

        n = -1
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')
        n = 0
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '0')
        n = 1
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '1')
        n = 500000
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '4151504')
        n = 999999
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '11333310')
        n = 1000000
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), '11333311')
        n = 1000001
        b = 7
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')

        n = -1
        b = 15
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')
        n = 0
        b = 15
        self.assertEqual(baseconverter.convert_number(n,b), '0')
        n = 1
        b = 15
        self.assertEqual(baseconverter.convert_number(n,b), '1')
        n = 500000
        b = 15
        self.assertEqual(baseconverter.convert_number(n,b), '9D235')
        n = 999999
        b = 15
        self.assertEqual(baseconverter.convert_number(n,b), '14B469')
        n = 1000000
        b = 15
        self.assertEqual(baseconverter.convert_number(n,b), '14B46A')
        n = 1000001
        b = 15
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')

        n = -1
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')
        n = 0
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), '0')
        n = 1
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), '1')
        n = 500000
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), '7A120')
        n = 999999
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), 'F423F')
        n = 1000000
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), 'F4240')
        n = 1000001
        b = 16
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number')
    
        n = -1
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number and base')
        n = 0
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 1
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 500000
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 999999
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 1000000
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid base')
        n = 1000001
        b = 17
        self.assertEqual(baseconverter.convert_number(n,b), 'Invalid number and base')


if __name__ == '__main__':
    unittest.main(verbosity=2)
