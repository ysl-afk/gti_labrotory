import unittest
from solver import calculate_compound_interest

class TestInterestCalculation(unittest.TestCase):

    def test_standard_calculation(self):
        # Проверяем обычный расчет: 10000 под 10% на 2 года
        # Ожидаем: 10000 * (1.1)^2 = 12100.00
        result = calculate_compound_interest(10000, 10, 2)
        self.assertEqual(result, "Через 2 лет итоговая сумма составит: 12100.00 руб.")

    def test_zero_time(self):
        # Проверяем случай, если срок 0 лет (сумма не должна измениться)
        result = calculate_compound_interest(50000, 15, 0)
        self.assertEqual(result, "Через 0 лет итоговая сумма составит: 50000.00 руб.")

    def test_zero_rate(self):
        # Проверяем случай с нулевой ставкой (сумма не должна измениться)
        result = calculate_compound_interest(1000, 0, 5)
        self.assertEqual(result, "Через 5 лет итоговая сумма составит: 1000.00 руб.")

    def test_invalid_input(self):
        # Проверяем, что программа выдает ошибку при вводе текста вместо чисел
        # Используем assertRaises, как в примере из лабы
        with self.assertRaises(TypeError):
            calculate_compound_interest("тысяча", 10, 2)

if __name__ == '__main__':
    unittest.main()