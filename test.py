import unittest


class TestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10,0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = area(10,10)
        self.assertEqual(res,50 )
    def test_perimeter(self):
        res = perimeter(3,4,5)
        self.assertEqual(res,12)
