import unittest
from .demo import addition


class TestAddition(unittest.TestCase):
    def test_addition(self):
        s = addition(10, 20)
        self.assertEqual(s, 30)

    def test_additio_failcase(self):
        s = addition(0,2)
        self.assertEqual(s, "nonnn")

    def test_additio_failcase1(self):
        s = addition(" ",2)
        self.assertEqual(s, "enter integer")



if __name__  == "__main__":
    unittest.main()