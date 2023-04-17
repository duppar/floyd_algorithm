"""
file to set up unittest for the add_in_lengths function
"""
import unittest
import sys

path1 = "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\\sw developement\\floyd_algorithm\\code"
sys.path.append(path1)
from shortest_path import add_in_lengths


class TestOutputCorrect(unittest.TestCase):
    """Class to test whether the output from the function is correct"""

    def setUp(self):
        print("set up")
        self.listlengths1 = [[0, 1, 3], [0, 3, 5], [1, 2, 5], [2, 3, 9]]
        self.input_graph = [
            [0, 99999, 99999, 99999],
            [99999, 0, 99999, 99999],
            [99999, 99999, 0, 99999],
            [99999, 99999, 99999, 0],
        ]

    def tearDown(self):
        print("tear down")

    def test_add_in_lengths(self):
        """test to see if the route lengths are added in correctly"""
        self.assertEqual(
            add_in_lengths(self.listlengths1, self.input_graph),
            [
                [0, 3, 99999, 5],
                [99999, 0, 5, 99999],
                [99999, 99999, 0, 9],
                [99999, 99999, 99999, 0],
            ],
        )


# set up unittest as main
if __name__ == "__main__":
    unittest.main()
