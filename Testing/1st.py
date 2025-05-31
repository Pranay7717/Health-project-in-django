def calculator(operand, number1, number2):
    if operand == "+":
        return number1 + number2
    elif operand == "-":
        return number1 - number2
    elif operand == "*":
        return number1 * number2
    elif operand == "/":
        if number2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return number1 / number2
    elif operand == "%":
        return number1 % number2
    elif operand == "**":
        return number1 ** number2
    else:
        raise ValueError("Invalid operand")


#testing

import unittest

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(calculator("+", 3, 2), 5)

    def test_subtraction(self):
        self.assertEqual(calculator("-", 5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(calculator("*", 4, 3), 12)

    def test_division(self):
        self.assertEqual(calculator("/", 10, 2), 5)

    def test_modulo(self):
        self.assertEqual(calculator("%", 10, 3), 1)

    def test_exponent(self):
        self.assertEqual(calculator("**", 2, 3), 8)

    def test_invalid_operand(self):
        with self.assertRaises(ValueError):
            calculator("&", 4, 2)

if __name__ == '__main__':
    unittest.main()
