import unittest
from infinity.base import series

class TestSeriesDecorator(unittest.TestCase):

    def test_series_decorator(self):

        @series(1)
        def great(a, n):
            return a + n

        g = great()
        self.assertEqual(1, next(g))
        self.assertEqual(2, next(g))
        self.assertEqual(3, next(g))
