import unittest

from main import part_one, part_two


class TestTheDay(unittest.TestCase):

    def setUp(self):
        self.data = []

    def test_part_one(self):
        self.assertTrue(part_one() is None)

    def test_part_two(self):
        self.assertTrue(part_two() is None)


if __name__ == '__main__':
    unittest.main()
