import unittest
import simpleCalculator


class SimpleCalculatorTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2, simpleCalculator.calc(1, 1, '+'), "Must be 2")

    def test_subtraction(self):
        self.assertEqual(0, simpleCalculator.calc(1, 1, '-'), "Must be 0")

    def test_multiplication(self):
        self.assertEqual(6, simpleCalculator.calc(3, 2, '*'), "Must be 6")

    def test_division(self):
        self.assertEqual(.5, simpleCalculator.calc(1, 2, '/'), "Must be .5")

    def test_non_number_input(self):
        self.assertEqual("ERROR: Input must follow format of (number, number, operation)",
                         simpleCalculator.calc(1, "3", '+'), "Must be ERROR")

    def test_float(self):
        self.assertEqual(2, simpleCalculator.calc(1, .5, '/'), "Must be 2")

    def test_divide_by_zero(self):
        self.assertEqual("ERROR: Cannot divide by 0", simpleCalculator.calc(1, 0, '/'), "Must be ERROR")

    def test_unexpected_operation(self):
        self.assertEqual("ERROR: Valid operations are +, -, *, and /", simpleCalculator.calc(1, 2, 'r'),
                         "Must be ERROR")


if __name__ == '__main__':
    unittest.main()