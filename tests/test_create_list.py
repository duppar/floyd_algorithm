import sys
import unittest


sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)


from shortest_path import create_list


# import running_Floyd    # The code to test
# import FloydR_run    # The code to test
# from FloydR4 import find_shortest_path


class TestOutputCorrect(unittest.TestCase):
    def setUp(self):
        print("set up")
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

    def tearDown(self):
        print("tear down")

    def test_create_list(self):
        self.assertEqual(create_list(1), self.output1)

    def test_create_list(self):
        self.assertEqual(create_list(2), self.output2)

    def test_create_list(self):
        self.assertEqual(create_list(3), self.output3)

    def test_create_list(self):
        self.assertEqual(create_list(4), self.output4)

    def test_create_list(self):
        self.assertEqual(create_list(5), self.output5)


if __name__ == "__main__":
    unittest.main()
