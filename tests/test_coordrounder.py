import unittest

from src.coordrounder import *

class TestCoordRounder(unittest.TestCase):
    def test_round_coord(self):
        self.assertEqual(round_coord(0.5), 0.5)
        self.assertEqual(round_coord(0.25), 0.25)
        self.assertEqual(round_coord(-0.85), -1.0)
        self.assertEqual(round_coord(0.282), 0.5)
        self.assertEqual(round_coord(0.24), 0.25)
        self.assertEqual(round_coord(0.05), 0.0625)
        self.assertEqual(round_coord(0.07), 0.125)
        self.assertEqual(round_coord(0.0625), 0.0625)
        self.assertEqual(round_coord(0.75562), 1.0)
        self.assertEqual(round_coord(-0.384), -0.5)

if __name__ == '__main__':
    unittest.main()