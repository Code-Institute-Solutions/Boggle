import unittest
from string import ascii_uppercase
import boggle


class TestBoggle(unittest.TestCase):
    """
    Our test case for boggle solver
    """

    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty boggle
        grid
        """
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid), 0)

    def test_grid_size_is_width_times_height(self):
        """
        Test to ensure that the total size of the grid is
        equal to width * height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)

    def test_grid_coordinates(self):
        """
        Test to ensure that all of the coordinates
        inside of the grid can be accessed
        """
        grid = boggle.make_grid(2, 2)
        self.assertTrue((0, 0) in grid)
        self.assertTrue((0, 1) in grid)
        self.assertTrue((1, 0) in grid)
        self.assertTrue((1, 1) in grid)
        self.assertTrue((2, 2) not in grid)

    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the grid contains
        letters
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertTrue(letter in ascii_uppercase)


if __name__ == '__main__':
    unittest.main()
