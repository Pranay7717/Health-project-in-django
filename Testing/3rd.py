def check_even_odd(a):
   if a % 2 == 0:
        return f"The given number {a} is even number"
    else:
        return f"The given number {a} is odd number"
      
#testing
import unittest

class TestEvenOdd(unittest.TestCase):
    
    def test_even(self):
        self.assertEqual(is_even_or_odd(4), "even")
        self.assertEqual(is_even_or_odd(100), "even")

    def test_odd(self):
        self.assertEqual(is_even_or_odd(5), "odd")
        self.assertEqual(is_even_or_odd(77), "odd")

    def test_zero(self):
        self.assertEqual(is_even_or_odd(0), "even")

if __name__ == '__main__':
    unittest.main()
