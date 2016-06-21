import unittest

from factorial import factorial_simple

"""
implement a fun function that adds one to a number.

start with 3, call fun, answer should be 4.
start with -2, call fun, answer should be -1.
start with 0, call fun, answer should be 1.
"""
def sum(n):
    sum = 0
    while n > 0:
       sum = sum + n
       n = n - 1
    return sum

def fun(n):
    return n + 1

def square(x):
    """Return the square of x.
    """
    return x * x

class FactorialTest(unittest.TestCase):

    def test(self):
        self.assertEqual(120, factorial_simple(5))
        self.assertEqual(1, factorial_simple(0))
        self.assertEqual(None, factorial_simple(-1))
        self.assertEqual(1, factorial_simple(1))
        self.assertEqual(2, factorial_simple(2))
        self.assertEqual(6, factorial_simple(3))
        self.assertEqual(24, factorial_simple(4))

class SumTest(unittest.TestCase):

    def test(self):
        self.assertEqual(5050, sum(100))

class FunTest(unittest.TestCase):

    def test(self):
        self.assertEqual(4, fun(3))
        self.assertEqual(-1, fun(-2))
        self.assertEqual(1, fun(0))

class SquareTest(unittest.TestCase):

    def test(self):
        self.assertEqual(4, square(2))
        self.assertEqual(4, square(-2))
        self.assertEqual(0, square(0))

if __name__ == '__main__':
    unittest.main()
