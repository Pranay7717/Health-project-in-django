def circle_area(radius):
    return 3.14 * radius ** 2

import unittest

class TestCircleArea(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertAlmostEqual(circle_area(1), 3.14)

    def test_area_zero_radius(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_float_radius(self):
        self.assertEqual(circle_area(2.5), 3.14 * 2.5 ** 2)

if __name__ == '__main__':
    unittest.main()
