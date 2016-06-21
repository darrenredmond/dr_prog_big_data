import unittest

class Calculator(object):
 
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def subtract(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError

# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

	# this tests the add functionality
	# 2 + 2 = 4
	# 2 + 4 = 6
	# 2 + (-2) = 0
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)

	#def test_calculator_returns_error_message_if_both_args_not_numbers(self):
    #    self.assertRaises(ValueError, self.calc.add, 'two', 'three')
    #    self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')

if __name__ == '__main__':
    unittest.main()
