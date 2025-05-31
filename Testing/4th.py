def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

import unittest

class TestLeapYear(unittest.TestCase):
    def test_leap_years(self):
        self.assertTrue(leap_year(2024))

    def test_non_leap_years(self):
        self.assertFalse(leap_year(2000))
if __name__ == '__main__':
    unittest.main()