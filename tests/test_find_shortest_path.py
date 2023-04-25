"""
file to set up unittest for the shortest_path function
"""
import sys
import unittest

sys.path.append(
    "C:\\Users\\xxxxxxx\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)
from shortest_path import find_shortest_path


class TestOutputCorrect(unittest.TestCase):
    """Unit tests to chect shortest path function is working correctly"""

    # set up
    def setUp(self):
        # Test case 19
        self.graph_correct_1 = [
            [0, 2, 99999, 2],
            [99999, 0, 3, 99999],
            [99999, 99999, 0, 1],
            [99999, 99999, 99999, 0],
        ]
        # Test case 20
        self.graph_correct_2 = [
            [0, 3, 99999, 6],
            [99999, 0, 1, 99999],
            [99999, 99999, 0, 1],
            [99999, 99999, 99999, 0],
        ]
        # Test case 21
        self.graph_correct_3 = [
            [0, 5, 99999, 4],
            [99999, 0, 1, 99999],
            [99999, 99999, 0, 6],
            [99999, 99999, 99999, 0],
        ]
        # Test case 22
        self.graph_correct_4 = [
            [0, 99999, 99999, 2],
            [3, 0, 2, 99999],
            [99999, 99999, 0, 5],
            [99999, 99999, 99999, 0],
        ]
        # Test case 23
        self.graph_correct_5 = [
            [0, 2, 99999, 2],
            [99999, 0, 2, 99999],
            [99999, 99999, 0, 99999],
            [99999, 99999, 3, 0],
        ]
        # Test case 24
        self.graph_correct_6 = [
            [0, 4, 99999, 3],
            [99999, 0, 8, 99999],
            [99999, 99999, 0, 7],
            [99999, 99999, 99999, 0],
        ]

        # Test case 25
        self.graph_correct_7 = [
            [10000, 400000, 99999, 3000],
            [99999, 0, 80000, 99999],
            [99999, 99999, 0, 70000],
            [99999, 99999, 99999, 0],
        ]
        # Test case 26 & 1
        self.graph_value_1 = [
            [0, 2, 99999, 4],
            [99999, 0, 2, 99999],
            [99999, 99999, 0, 3],
            [99999, 99999, 99999, 0],
        ]
        # Test case 27 & 2
        self.graph_value_2 = [
            [0, 7.9, 9, 99999],
            [99999, 0, 2.8, 99999],
            [99999, 0.2, 0, 99999],
            [0.4, 99999, 99999, 0],
        ]
        # Test case 28 & 3
        self.graph_value_3 = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        # Test case 29 & 4
        self.graph_value_4 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        # Test case 30 & 5
        self.graph_value_5 = [
            [0, -4, 6, 99999],
            [-2, 0, 99999, 10],
            [99999, 3, 0, 99999],
            [99999, 5, 99999, 0],
        ]
        # Test case 31 & 6
        self.graph_value_6 = [
            [0, 4, 6, 99999],
            [2, 0, 6, 99999],
            [99999, 3, 0, 3],
            [3, 99999, 6, 0],
        ]
        # Test case 32 & 7
        self.graph_value_7 = [
            [0, 2, 1, 3],
            [99999, 0, 2, 99999],
            [99999, 99999, 0, 1],
            [99999, 99999, 99999, 0],
        ]
        # Test case 8
        self.output_1 = [
            [99999],
        ]
        # Test case 9
        self.output_2 = [
            [99999, 99999],
            [99999, 99999],
        ]
        # Test case 10
        self.output_3 = [
            [99999, 99999, 99999],
            [99999, 99999, 99999],
            [99999, 99999, 99999],
        ]
        # Test case 11
        self.output_4 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        # Test case 12
        self.output_5 = [
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
        ]
        # Test case 14
        self.output_value_1 = [
            [0],
        ]
        # Test case 15
        self.output_value_2 = [
            [0, 1],
            [99999, 0],
        ]
        # Test case 16
        self.output_value_3 = [
            [0, 1, 2],
            [99999, 0, 3],
            [99999, 99999, 0],
        ]
        # Test case 17
        self.output_value_4 = [
            [0, 2, 99999, 3],
            [99999, 0, 99999, 99999],
            [99999, 2, 0, 99999],
            [99999, 99999, 2, 0],
        ]
        # Test case 18
        self.output_value_5 = [
            [0, 99999, 2, 99999, 99999],
            [99999, 0, 3, 99999, 99999],
            [99999, 99999, 0, 99999, 7],
            [99999, 5, 99999, 0, 99999],
            [99999, 99999, 99999, 99999, 0],
        ]
        self.i = 0
        self.j = 0
        self.k = 0

    # tear down
    def tearDown(self):
        self.graph_correct_1 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_correct_2 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_correct_3 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_correct_4 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_correct_5 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_correct_6 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_correct_7 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_value_1 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_value_2 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_value_3 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_value_4 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_value_5 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_value_6 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.graph_value_7 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.output_1 = [
            [99999],
        ]
        self.output_2 = [
            [99999, 99999],
            [99999, 99999],
        ]
        self.output_3 = [
            [99999, 99999, 99999],
            [99999, 99999, 99999],
            [99999, 99999, 99999],
        ]
        self.output_4 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.output_5 = [
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
        ]
        self.output_value_1 = [
            [99999],
        ]
        self.output_value_2 = [
            [99999, 99999],
            [99999, 99999],
        ]
        self.output_value_3 = [
            [99999, 99999, 99999],
            [99999, 99999, 99999],
            [99999, 99999, 99999],
        ]
        self.output_value_4 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.output_value_5 = [
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999, 99999],
        ]
        self.i = 0
        self.j = 0
        self.k = 0

    # Tests to check the function returns a value
    def test_path_returned_1(self):
        """Test a value is returned
        Test example equal length paths graph returns a value (test 1)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_1, 4)
        )

    def test_path_returned_2(self):
        """Test a value is returned
        Test example float graph returns a value (test 2)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_2, 4)
        )

    def test_path_returned_3(self):
        """Test a value is returned
        Test same weigth input graph returns a value (test 3)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_3, 4)
        )

    def test_path_returned_4(self):
        """Test a value is returned
        Test no path input graph returns a value (test 4)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_4, 4)
        )

    def test_path_returned_5(self):
        """Test a value is returned
        Test negative path input graph returns a value (test 5)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_5, 4)
        )

    def test_path_returned_6(self):
        """Test a value is returned
        Test bidirectional path input graph returns a value (test 6)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_6, 4)
        )

    def test_path_returned_7(self):
        """Test a value is returned
        Test diagnol/1 to all nodes path input graph returns a value (test 7)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_7, 4)
        )

    # Test different number of graph nodes works (test 8)

    def ntest_node_number_1(self):
        """Test a value is returned
        Test 1 graph nodes works removed as no path with one node"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_1, 1)
        )

    def test_node_number_2(self):
        """Test a value is returned
        Test 2 graph nodes works (test 9)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_2, 2)
        )

    def test_node_number_3(self):
        """Test a value is returned
        Test 3 graph nodes works (test 10)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_3, 3)
        )

    def test_node_number_4(self):
        """Test a value is returned
        Test 4 graph nodes works (test 11)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_4, 4)
        )

    def test_node_number_5(self):
        """Test a value is returned
        Test 5 graph nodes works (test 12)"""
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_5, 5)
        )

    # Test path output from number of graph nodes works
    def ntest_node_number_value_1(self):
        """Test a value is returned
        Test 1 graph nodes works (test 14) removed as 1 node is not a route"""
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_1, 1),
            [
                [0],
            ],
        )

    def test_node_number_value_2(self):
        """Test a value returned is correct
        Test 2 graph nodes works (test 15)"""
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_2, 2),
            [
                [0, 1],
                [99999, 0],
            ],
        )

    def test_node_number_value_3(self):
        """Test a value returned is correct
        Test 3 graph nodes works (test 16)"""
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_3, 3),
            [
                [0, 1, 2],
                [99999, 0, 3],
                [99999, 99999, 0],
            ],
        )

    def test_node_number_value_4(self):
        """Test a value returned is correct
        Test 4 graph nodes works (test 17)"""
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_4, 4),
            [
                [0, 2, 5, 3],
                [99999, 0, 99999, 99999],
                [99999, 2, 0, 99999],
                [99999, 4, 2, 0],
            ],
        )

    def test_node_number_value_5(self):
        """Test a value returned is correct
        Test 5 graph nodes works (test 18)"""
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_5, 5),
            [
                [0, 99999, 2, 99999, 9],
                [99999, 0, 3, 99999, 10],
                [99999, 99999, 0, 99999, 7],
                [99999, 5, 8, 0, 15],
                [99999, 99999, 99999, 99999, 0],
            ],
        )

    # Test the values outputted for the shortest path are correct
    def test_output_paths_correct_1(self):
        """test shortest path is returned
        Test a range of integer graph inputs. (test 19)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_1, 4),
            [
                [0, 2, 5, 2],
                [99999, 0, 3, 4],
                [99999, 99999, 0, 1],
                [99999, 99999, 99999, 0],
            ],
        )

    def test_output_paths_correct_2(self):
        """test shortest path is returned
        Test a range of integer graph inputs. (test 20)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_2, 4),
            [
                [0, 3, 4, 5],
                [99999, 0, 1, 2],
                [99999, 99999, 0, 1],
                [99999, 99999, 99999, 0],
            ],
        )

    def test_output_paths_correct_3(self):
        """test shortest path is returned
        Test a range of integer graph inputs. (test 21)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_3, 4),
            [
                [0, 5, 6, 4],
                [99999, 0, 1, 7],
                [99999, 99999, 0, 6],
                [99999, 99999, 99999, 0],
            ],
        )

    def test_output_paths_correct_4(self):
        """test shortest path is returned
        Test a range of integer graph inputs. (test 22)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_4, 4),
            [
                [0, 99999, 99999, 2],
                [3, 0, 2, 5],
                [99999, 99999, 0, 5],
                [99999, 99999, 99999, 0],
            ],
        )

    def test_output_paths_correct_5(self):
        """test shortest path is returned
        Test a range of integer graph inputs. (test 23)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_5, 4),
            [
                [0, 2, 4, 2],
                [99999, 0, 2, 99999],
                [99999, 99999, 0, 99999],
                [99999, 99999, 3, 0],
            ],
        )

    def test_output_paths_correct_6(self):
        """test shortest path is returned
        Test a range of integer graph inputs. (test 24)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_6, 4),
            [
                [0, 4, 12, 3],
                [99999, 0, 8, 15],
                [99999, 99999, 0, 7],
                [99999, 99999, 99999, 0],
            ],
        )

    def test_output_paths_correct_7(self):
        """test shortest path is returned
        Test with large integers     (test 25)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_7, 4),
            [
                [10000, 102999, 99999, 3000],
                [99999, 0, 80000, 99999],
                [99999, 99999, 0, 70000],
                [99999, 99999, 99999, 0],
            ],
        )

    def test_path_correct_1(self):
        """test shortest path is returned
        Test example equal length paths graph returns a value (test 26)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_1, 4),
            [
                [0, 2, 4, 4],
                [99999, 0, 2, 5],
                [99999, 99999, 0, 3],
                [99999, 99999, 99999, 0],
            ],
        )

    def test_path_correct_2(self):
        """test shortest path is returned
        Test example float graph returns a value (test 27)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_2, 4),
            [
                [0, 7.9, 9, 99999],
                [99999, 0, 2.8, 99999],
                [99999, 0.2, 0, 99999],
                [0.4, 8.3, 9.4, 0],
            ],
        )

    def test_path_correct_3(self):
        """test shortest path is returned
        Test same weigth input graph returns a value (test 28)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_3, 4),
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
        )

    def test_path_correct_4(self):
        """test shortest path is returned
        Test no path input graph returns a value (test 29)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_4, 4),
            [
                [99999, 99999, 99999, 99999],
                [99999, 99999, 99999, 99999],
                [99999, 99999, 99999, 99999],
                [99999, 99999, 99999, 99999],
            ],
        )

    def test_path_correct_5(self):
        """test shortest path is returned
        Test negative path input graph returns a value (test 30)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_5, 4),
            [
                [0, -4, 0, 6],
                [-2, 0, 4, 10],
                [1, 3, 0, 13],
                [3, 5, 9, 0],
            ],
        )

    def test_path_correct_6(self):
        """test shortest path is returned
        Test bidirectional path input graph returns a value (test 31)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_6, 4),
            [[0, 4, 6, 9], [2, 0, 6, 9], [5, 3, 0, 3], [3, 7, 6, 0]],
        )

    def test_path_correct_7(self):
        """test shortest path is returned
        Test diagnol/1 to all nodes path input graph returns a value (test 32)
        """
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_7, 4),
            [
                [0, 2, 1, 2],
                [99999, 0, 2, 3],
                [99999, 99999, 0, 1],
                [99999, 99999, 99999, 0],
            ],
        )


if __name__ == "__main__":
    unittest.main()
