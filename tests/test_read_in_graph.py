"""
file to set up unittest for the read_in_graph function
"""
import sys
import unittest


sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)

from shortest_path import read_in_graph


class TestOutputCorrect(unittest.TestCase):
    """Unittesting to test the Graphs are read in correctly"""

    def setUp(self):
        self.i = 0
        self.j = 0
        self.k = 0

    def tearDown(self):
        self.i = 0
        self.j = 0
        self.k = 0

    def test_read_in_graph(self):
        """Test that graph is read in correctly"""
        self.assertEqual(read_in_graph(), [[0, 1, 2], [0, 3, 4], [1, 2, 2], [2, 3, 3]])


if __name__ == "__main__":
    unittest.main()
