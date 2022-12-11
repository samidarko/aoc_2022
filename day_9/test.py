import unittest

from main import part_two


class TestPartTwo(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]

    def test_part_two(self):
        self.assertEqual(part_two(self.matrix), 8)


if __name__ == '__main__':
    unittest.main()
