"""
file to set up unittest for the create_list function
"""
import sys
import unittest

sys.path.append(
    "C:\\Users\\610109025\\OneDrive - BT Plc\\Documents - RDM Admin\\General\\Post Grad\\sw developement\\floyd_algorithm\\code"
)
from shortest_path import create_list


class TestOutputCorrect(unittest.TestCase):
    """Test that correct list is created"""

    def setUp(self):
        """set up for create lst testing"""
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

    def test_create_list1(self):
        """Check list of length 1"""
        self.assertEqual(create_list(1), self.output1)

    def test_create_list2(self):
        """Check list of length 2"""
        self.assertEqual(create_list(2), self.output2)

    def test_create_list3(self):
        """Check list of length 3"""
        self.assertEqual(create_list(3), self.output3)

    def test_create_list4(self):
        """Check list of length 4"""
        self.assertEqual(create_list(4), self.output4)

    def test_create_list5(self):
        """Check list of length 5"""
        self.assertEqual(create_list(5), self.output5)


if __name__ == "__main__":
    unittest.main()
