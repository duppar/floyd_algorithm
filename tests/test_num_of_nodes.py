import sys
import unittest


sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)


from shortest_path import num_of_nodes


# import running_Floyd    # The code to test
# import FloydR_run    # The code to test
# from FloydR4 import find_shortest_path


class TestOutputCorrect(unittest.TestCase):
    def setUp(self):
        print("set up")
        self.listlengths1 = [[0, 1, 3], [0, 3, 5], [1, 2, 5], [2, 3, 9]]

    def tearDown(self):
        print("tear down")

    def test_num_of_nodes(self):
        self.assertEqual(num_of_nodes(self.listlengths1), 3)
        # self.assertEqual(funcinout.graph, 4)


# def test_decrement(self):
# self.assertEqual(inc_dec.decrement(3), 4)
# to capture testfiles
if __name__ == "__main__":
    unittest.main()
