import sys
import unittest


sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)


from shortest_path import add_in_lengths

# import running_Floyd    # The code to test
# import FloydR_run    # The code to test
# from FloydR4 import find_shortest_path


class TestOutputCorrect(unittest.TestCase):
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
        self.assertEqual(
            add_in_lengths(self.listlengths1, self.input_graph),
            [
                [0, 3, 99999, 5],
                [99999, 0, 5, 99999],
                [99999, 99999, 0, 9],
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
