def weird_check(n):
    if (n % 2) != 0:
        return "Weird"
    else:
        if n >= 2 and n <= 5:
            return "Not Weird"
        elif n >= 6 and n <= 20:
            return "Weird"
        else:
            return "Not Weird"
    
 #testing

import unittest

class TestWeirdChecker(unittest.TestCase):
    def test_odd_numbers(self):
        self.assertEqual(weird_check(3), "Weird")

    def test_even_2_to_5(self):
        self.assertEqual(weird_check(2), "Not Weird")

    def test_even_6_to_20(self):
        self.assertTrue(weird_check(6), "Weird")

    def test_even_greater_than_20(self):
        self.assertEqual(weird_check(22), "Not Weird")

if __name__ == '__main__':
    unittest.main()
