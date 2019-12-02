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

    def test_round_coord_more_that_one(self):
        self.assertEqual(round_coord(1.5), 1.5)
        self.assertEqual(round_coord(2.25), 2.25)
        self.assertEqual(round_coord(-34.85), -35.0)
        self.assertEqual(round_coord(2.282), 2.5)
        self.assertEqual(round_coord(1.24), 1.25)
        self.assertEqual(round_coord(3.05), 3.0625)
        self.assertEqual(round_coord(23434.07), 23434.125)
        self.assertEqual(round_coord(1.0625), 1.0625)
        self.assertEqual(round_coord(1.75562), 2.0)
        self.assertEqual(round_coord(-2.384), -2.5)

if __name__ == '__main__':
    unittest.main()