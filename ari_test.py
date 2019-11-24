import unittest
from .ari import Arithmetic


class TestArithmetic(unittest.TestCase):

    def setUp(self):
        pass

    def test_addition(self):
        s = Arithmetic()
        result = s.addition(10, 20)
        self.assertEqual(result, 30)

    def test_addition1(self):
        s = Arithmetic()
        result = s.addition()
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()