"""
file to set up unittest for the num_of_nodes function
"""
import sys
import unittest

sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)

from shortest_path import num_of_nodes


class TestOutputCorrect(unittest.TestCase):
    """Test to check number of nodes function"""

    def setUp(self):
        self.listlengths1 = [[0, 1, 3], [0, 3, 5], [1, 2, 5], [2, 3, 9]]

    def tearDown(self):
        self.listlengths1 = [[0, 1, 3], [0, 3, 5], [1, 2, 5], [2, 3, 9]]

    def test_num_of_nodes(self):
        """Checks that the number of nodes is correct"""
        self.assertEqual(num_of_nodes(self.listlengths1), 3)


if __name__ == "__main__":
    unittest.main()
