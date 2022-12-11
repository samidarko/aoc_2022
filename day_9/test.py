import unittest

from main import part_two


class TestPartTwo(unittest.TestCase):

    def setUp(self):
        self.instructions = [line.strip() for line in open("test_input.txt").readlines()]

    def test_part_two(self):
        result = part_two(self.instructions)
        self.assertEqual(len(set(result)), 36)


if __name__ == '__main__':
    unittest.main()
