import unittest
from program2 import program2

class TestAlgo2(unittest.TestCase):
    def test_case_1(self):
        n = 7
        W = 10
        heights = [21, 19, 17, 16, 11, 5, 1]
        widths = [7, 1, 2, 3, 5, 8, 1]
        expected_platforms = 3
        expected_cost = 42
        expected_sculptures_per_platform = [3, 2, 2]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_2(self):
        n = 5
        W = 10
        heights = [15, 10, 5, 10, 15]
        widths = [2, 2, 2, 2, 2]
        expected_platforms = 1
        expected_cost = 15
        expected_sculptures_per_platform = [5]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_3(self):
        n = 7
        W = 10
        heights = [12, 10, 9, 7, 8, 10, 11]
        widths = [3, 2, 3, 4, 3, 2, 3]
        expected_platforms = 3
        expected_cost = 30
        expected_sculptures_per_platform = [3, 1, 3]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_4(self):
        n = 1
        W = 5
        heights = [5]
        widths = [3]
        expected_platforms = 1
        expected_cost = 5
        expected_sculptures_per_platform = [1]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_6(self):
        n = 5
        W = 10
        heights = [15, 15, 10, 5, 10]
        widths = [2, 2, 2, 2, 2]
        expected_platforms = 1
        expected_cost = 15
        expected_sculptures_per_platform = [5]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_7(self):
        n = 6
        W = 10
        heights = [35, 15, 15, 5, 10, 10]
        widths = [1, 2, 3, 4, 5, 6]
        expected_platforms = 3
        expected_cost = 55
        expected_sculptures_per_platform = [4, 1, 1]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_8(self):
        n = 6
        W = 10
        heights = [35, 15, 15, 5, 10, 10]
        widths = [1, 2, 3, 4, 5, 5]
        expected_platforms = 2
        expected_cost = 45
        expected_sculptures_per_platform = [4, 2]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_9(self):
        n = 6
        W = 10
        heights = [35, 15, 15, 5, 10, 10]
        widths = [1, 2, 3, 5, 4, 6]
        expected_platforms = 3
        expected_cost = 50
        expected_sculptures_per_platform = [3, 1, 2]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_10(self):
        n = 5
        W = 10
        heights = [35, 15, 15, 5, 10]
        widths = [1, 2, 3, 5, 4]
        expected_platforms = 2
        expected_cost = 45
        expected_sculptures_per_platform = [3, 2]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_11(self):
        n = 6
        W = 10
        heights = [35, 15, 15, 5, 10, 10]
        widths = [1, 2, 3, 5, 4, 7]
        expected_platforms = 3
        expected_cost = 55
        expected_sculptures_per_platform = [3, 2, 1]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_12(self):
        # multiple possible solutions
        n = 5
        W = 10
        heights = [35, 15, 15, 5, 10]
        widths = [4, 3, 2, 1, 1]
        expected_platforms = 2
        expected_cost = 45
        expected_sculptures_per_platform = [4, 1]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_13(self):
        # multiple possible solutions
        n = 6
        W = 10
        heights = [35, 15, 10, 5, 15, 20]
        widths = [3, 3, 2, 1, 1, 1]
        expected_platforms = 2
        expected_cost = 55
        expected_sculptures_per_platform = [4, 2]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")

    def test_case_14(self):
        # multiple possible solutions
        n = 6
        W = 10
        heights = [35, 15, 10, 5, 10, 15]
        widths = [3, 3, 2, 1, 1, 10]
        expected_platforms = 2
        expected_cost = 50
        expected_sculptures_per_platform = [5, 1]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, f"Expected {expected_platforms} platforms, but received {platforms}.")
        self.assertEqual(cost, expected_cost, f"Expected {expected_cost} total height cost, but received {cost}.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, f"Expected {expected_sculptures_per_platform} sculptures per platform, but received {sculptures_per_platform}.")

    def test_case_15(self):
        # multiple possible solutions
        n = 6
        W = 10
        heights = [35, 15, 10, 5, 75, 85]
        widths = [3, 3, 2, 1, 1, 1]
        expected_platforms = 2
        expected_cost = 120
        expected_sculptures_per_platform = [4, 2]

        platforms, cost, sculptures_per_platform = program2(n, W, heights, widths)

        self.assertEqual(platforms, expected_platforms, "Number of platforms does not match the expected value.")
        self.assertEqual(cost, expected_cost, "Total height does not match the expected value.")
        self.assertEqual(sculptures_per_platform, expected_sculptures_per_platform, "Sculptures per platform do not match the expected value.")


if __name__ == "__main__":
    unittest.main()
