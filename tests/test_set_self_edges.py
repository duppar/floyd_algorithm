"""
file to set up unittest for the set_self_edges function
"""
import sys
import unittest


sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)


from shortest_path import set_self_edge


# import running_Floyd    # The code to test
# import FloydR_run    # The code to test
# from FloydR4 import find_shortest_path


class TestOutputCorrect(unittest.TestCase):
    def setUp(self):
        print("set up")
        self.input_graph = [
            [0, 99999, 99999, 99999],
            [99999, 0, 99999, 99999],
            [99999, 99999, 0, 99999],
            [99999, 99999, 99999, 0],
        ]

    def tearDown(self):
        print("tear down")

    def test_set_self_edge(self):
        self.assertEqual(
            set_self_edge(4, self.input_graph),
            [
                [0, 99999, 99999, 99999],
                [99999, 0, 99999, 99999],
                [99999, 99999, 0, 99999],
                [99999, 99999, 99999, 0],
            ],
        )
        # self.assertEqual(funcinout.graph, 4)

    # This test is designed to fail for demonstration purposes.


# def test_decrement(self):
# self.assertEqual(inc_dec.decrement(3), 4)
# to capture testfiles
if __name__ == "__main__":
    unittest.main()


# [[0, 10, 15, 4], [99999, 0, 5, 12], [99999, 99999, 0, 7], [99999, 99999, 99999, 0]]
