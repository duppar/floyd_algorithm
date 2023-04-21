"""
file to set up unittest for the set_self_edges function
"""
import sys
import unittest


sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)

from shortest_path import set_self_edge


class TestOutputCorrect(unittest.TestCase):
    """tests to check nodes are set to zero for themselves"""

    def setUp(self):
        self.input_graph = [
            [0, 99999, 99999, 99999],
            [99999, 0, 99999, 99999],
            [99999, 99999, 0, 99999],
            [99999, 99999, 99999, 0],
        ]

    def tearDown(self):
        self.input_graph = [
            [0, 99999, 99999, 99999],
            [99999, 0, 99999, 99999],
            [99999, 99999, 0, 99999],
            [99999, 99999, 99999, 0],
        ]

    def test_set_self_edge(self):
        """check that the self vertex are set to zero"""
        self.assertEqual(
            set_self_edge(4, self.input_graph),
            [
                [0, 99999, 99999, 99999],
                [99999, 0, 99999, 99999],
                [99999, 99999, 0, 99999],
                [99999, 99999, 99999, 0],
            ],
        )


if __name__ == "__main__":
    unittest.main()
