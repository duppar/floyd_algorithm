import sys
import unittest


sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)

from shortest_path import read_in_graph


# import running_Floyd    # The code to test
# import FloydR_run    # The code to test
# from FloydR4 import find_shortest_path


class TestOutputCorrect(unittest.TestCase):
    def setUp(self):
        print("set up")
        self.i = 0
        self.j = 0
        self.k = 0

    def tearDown(self):
        print("tear down")
        self.i = 0
        self.j = 0
        self.k = 0

    def test_read_in_graph(self):
        self.assertEqual(read_in_graph(), [[0, 1, 3], [0, 3, 5], [1, 2, 5], [2, 3, 9]])
        # self.assertEqual(funcinout.graph, 4)


# def test_decrement(self):
# self.assertEqual(inc_dec.decrement(3), 4)
# to capture testfiles
if __name__ == "__main__":
    unittest.main()
