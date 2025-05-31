def multiply(n):
    result = []
    for i in range(1, 11):
        result.append(f"{n} x {i} = {n * i}")
    return result

# testing 

import unittest

class TestMultiplyTable(unittest.TestCase):
    
    def test_table_of_2(self):
        expected = [
            "2 x 1 = 2",
            "2 x 2 = 4",
            "2 x 3 = 6",
            "2 x 4 = 8",
            "2 x 5 = 10",
            "2 x 6 = 12",
            "2 x 7 = 14",
            "2 x 8 = 16",
            "2 x 9 = 18",
            "2 x 10 = 20"
        ]
        self.assertEqual(multiply(2), expected)

    def test_table_of_5(self):
        expected = [
            "5 x 1 = 5",
            "5 x 2 = 10",
            "5 x 3 = 15",
            "5 x 4 = 20",
            "5 x 5 = 25",
            "5 x 6 = 30",
            "5 x 7 = 35",
            "5 x 8 = 40",
            "5 x 9 = 45",
            "5 x 10 = 50"
        ]
        self.assertEqual(multiply(5), expected)

if __name__ == '__main__':
    unittest.main()
