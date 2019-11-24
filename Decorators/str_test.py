import unittest
from . import str_upper

class Check(unittest.TestCase):
    def test_string(self):
        s = print(str_upper.print_str("vinod"))
        print(s)
        self.assertEqual(s, "VINOD")



if __name__ == '__main__':
    unittest.main()