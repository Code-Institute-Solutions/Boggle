import unittest
import boggle


class TestBoggle(unittest.TestCase):
    """
    Our test case for boggle solver
    """

    def test_is_this_thing_on(self):
        """
        Simple test to ensure that the tests are
        correctly linked to `boggle.py`
        """
        self.assertEqual(1, boggle.check())


if __name__ == '__main__':
    unittest.main()