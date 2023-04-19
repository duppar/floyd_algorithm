"""
file to set up unittest for the shortest_path function
"""
import sys
import unittest


sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)

from shortest_path import find_shortest_path


class TestOutputCorrect(unittest.TestCase):
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
        self.output_n = "pull ths is from file??"
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
        self.output1 = [
            [99999],
        ]
        self.output2 = [
            [99999, 99999],
            [99999, 99999],
        ]
        self.output3 = [
            [99999, 99999, 99999],
            [99999, 99999, 99999],
            [99999, 99999, 99999],
        ]
        self.output4 = [
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
            [99999, 99999, 99999, 99999],
        ]
        self.output5 = [
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
    # Test example equal length paths graph returns a value (test 1)
    def test_path_returned_1(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_1, 4)
        )

    # Test example float graph returns a value (test 2)
    def test_path_returned_2(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_2, 4)
        )

    # Test same weigth input graph returns a value (test 3)
    def test_path_returned_3(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_3, 4)
        )

    # Test no path input graph returns a value (test 4)
    def test_path_returned_4(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_4, 4)
        )

    # Test negative path input graph returns a value (test 5)
    def test_path_returned_5(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_5, 4)
        )

    # Test bidirectional path input graph returns a value (test 6)
    def test_path_returned_6(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_6, 4)
        )

    # Test diagnol/1 to all nodes path input graph returns a value (test 7)
    def test_path_returned_7(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_7, 4)
        )

    # Test different number of graph nodes works (test 8)
    # Test 1 graph nodes works removed as no path with one node
    def ntest_node_number_1(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_1, 1)
        )

    # Test 2 graph nodes works (test 9)
    def test_node_number_2(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_2, 2)
        )

    # Test 3 graph nodes works (test 10)
    def test_node_number_3(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_3, 3)
        )

    # Test 4 graph nodes works (test 11)
    def test_node_number_4(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_4, 4)
        )

    # Test 5 graph nodes works (test 12)
    def test_node_number_5(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_5, 5)
        )

    # Test large n =50 graph nodes works n put in name so not picked up by testrunner (test 13)
    def ntest_node_number_n(self):
        self.assertIsNotNone(
            find_shortest_path(self.i, self.j, self.k, self.output_n, 5)
        )

    # Test path output from number of graph nodes works
    # Test 1 graph nodes works (test 14) removed as 1 node is not a route
    def ntest_node_number_value_1(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_1, 1),
            [
                [0],
            ],
        )

    # Test 2 graph nodes works (test 15)
    def test_node_number_value_2(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_2, 2),
            [
                [0, 1],
                [99999, 0],
            ],
        )

    # Test 3 graph nodes works (test 16)
    def test_node_number_value_3(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_3, 3),
            [
                [0, 1, 2],
                [99999, 0, 3],
                [99999, 99999, 0],
            ],
        )

    # Test 4 graph nodes works (test 17)
    def test_node_number_value_4(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.output_value_4, 4),
            [
                [0, 2, 5, 3],
                [99999, 0, 99999, 99999],
                [99999, 2, 0, 99999],
                [99999, 4, 2, 0],
            ],
        )

    # Test 5 graph nodes works (test 18)
    def test_node_number_value_5(self):
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
    # Test a range of integer graph inputs. (test 19)
    def test_output_paths_correct_1(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_1, 4),
            [
                [0, 2, 5, 2],
                [99999, 0, 3, 4],
                [99999, 99999, 0, 1],
                [99999, 99999, 99999, 0],
            ],
        )

    # Test a range of integer graph inputs. (test 20)
    def test_output_paths_correct_2(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_2, 4),
            [
                [0, 3, 4, 5],
                [99999, 0, 1, 2],
                [99999, 99999, 0, 1],
                [99999, 99999, 99999, 0],
            ],
        )

    # Test a range of integer graph inputs. (test 21)
    def test_output_paths_correct_3(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_3, 4),
            [
                [0, 5, 6, 4],
                [99999, 0, 1, 7],
                [99999, 99999, 0, 6],
                [99999, 99999, 99999, 0],
            ],
        )

    # Test a range of integer graph inputs. (test 22)
    def test_output_paths_correct_4(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_4, 4),
            [
                [0, 99999, 99999, 2],
                [3, 0, 2, 5],
                [99999, 99999, 0, 5],
                [99999, 99999, 99999, 0],
            ],
        )

    # Test a range of integer graph inputs. (test 23)
    def test_output_paths_correct_5(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_5, 4),
            [
                [0, 2, 4, 2],
                [99999, 0, 2, 99999],
                [99999, 99999, 0, 99999],
                [99999, 99999, 3, 0],
            ],
        )

    # Test a range of integer graph inputs. (test 24)
    def test_output_paths_correct_6(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_6, 4),
            [
                [0, 4, 12, 3],
                [99999, 0, 8, 15],
                [99999, 99999, 0, 7],
                [99999, 99999, 99999, 0],
            ],
        )

    # Test with large integers     (test 25)
    def test_output_paths_correct_7(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_correct_7, 4),
            [
                [10000, 102999, 99999, 3000],
                [99999, 0, 80000, 99999],
                [99999, 99999, 0, 70000],
                [99999, 99999, 99999, 0],
            ],
        )

    # Test example equal length paths graph returns a value (test 26)
    def test_path_correct_1(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_1, 4),
            [
                [0, 2, 4, 4],
                [99999, 0, 2, 5],
                [99999, 99999, 0, 3],
                [99999, 99999, 99999, 0],
            ],
        )

    # Test example float graph returns a value (test 27)
    def test_path_correct_2(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_2, 4),
            [
                [0, 7.9, 9, 99999],
                [99999, 0, 2.8, 99999],
                [99999, 0.2, 0, 99999],
                [0.4, 8.3, 9.4, 0],
            ],
        )

    # Test same weigth input graph returns a value (test 28)
    def test_path_correct_3(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_3, 4),
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
        )

    # Test no path input graph returns a value (test 29)
    def test_path_correct_4(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_4, 4),
            [
                [99999, 99999, 99999, 99999],
                [99999, 99999, 99999, 99999],
                [99999, 99999, 99999, 99999],
                [99999, 99999, 99999, 99999],
            ],
        )

    # Test negative path input graph returns a value (test 30)
    def test_path_correct_5(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_5, 4),
            [
                [0, -4, 0, 6],
                [-2, 0, 4, 10],
                [1, 3, 0, 13],
                [3, 5, 9, 0],
            ],
        )

    # Test bidirectional path input graph returns a value (test 31)
    def test_path_correct_6(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_6, 4),
            [[0, 4, 6, 9], [2, 0, 6, 9], [5, 3, 0, 3], [3, 7, 6, 0]],
        )

    # Test diagnol/1 to all nodes path input graph returns a value (test 32)
    def test_path_correct_7(self):
        self.assertEqual(
            find_shortest_path(self.i, self.j, self.k, self.graph_value_7, 4),
            [
                [0, 2, 1, 2],
                [99999, 0, 2, 3],
                [99999, 99999, 0, 1],
                [99999, 99999, 99999, 0],
            ],
        )


# tests values for different number of nodes


# to capture testfiles
if __name__ == "__main__":
    unittest.main()
