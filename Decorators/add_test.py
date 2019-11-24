import unittest
from .Add import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        s = add(2,4)
        self.assertEqual(s, 6)
        self.ass


if __name__ == "__main__":
    unittest.main()