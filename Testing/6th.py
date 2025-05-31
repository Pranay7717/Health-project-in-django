def check_positive_negative(n):
    if n < 0:
        return "it is negative"
    else:
        return "it is positive"




import unittest

class TestPosNegChecker(unittest.TestCase):
    
    def test_positive_number(self):
        self.assertTrue(check_positive_negative(10), "it is positive")

    def test_negative_number(self):
        self.assertNotEqual(check_positive_negative(5), "it is negative")

    def test_zero(self):
        self.assertEqual(check_positive_negative(0), "it is positive")  

if __name__ == '__main__':
    unittest.main()
