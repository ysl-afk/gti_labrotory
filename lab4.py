import unittest
from solver import calculate_compound_interest

class TestInterestCalculation(unittest.TestCase):

    def test_standard_calculation(self):
        result = calculate_compound_interest(10000, 10, 2)
        self.assertEqual(result, "Через 2 лет итоговая сумма составит: 12100.00 руб.")

    def test_zero_time(self):
        result = calculate_compound_interest(50000, 15, 0)
        self.assertEqual(result, "Через 0 лет итоговая сумма составит: 50000.00 руб.")

    def test_zero_rate(self):
        result = calculate_compound_interest(1000, 0, 5)
        self.assertEqual(result, "Через 5 лет итоговая сумма составит: 1000.00 руб.")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_compound_interest("тысяча", 10, 2)

if __name__ == '__main__':
    unittest.main()