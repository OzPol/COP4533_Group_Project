import unittest
import sys
# from program3 import program3 as program
# from program4 import program4 as program
# from program5B import program5B as program
from program5A import program5A as program

class TestProblemG(unittest.TestCase):
    def testcase_1(self):
        # example1 from pdf
        n = 7 
        W = 10
        heights = [21,19,17,16,11,5,1]
        widths = [7,1,2,3,5,8,1]

        expected_output = (3, 42, [3, 2, 2])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")
    
    def testcase_2(self):
        # example2 from pdf
        n = 4 
        W = 10
        heights = [8,10,9,7]
        widths = [8,1,2,2]

        expected_output = (2, 18, [1, 3])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_3(self):
        # example3 from pdf
        n = 7 
        W = 10
        heights = [12, 10, 9, 7, 8, 10, 11]
        widths = [3, 2, 3, 4, 3, 2, 3]

        expected_output = (3, 30, [3, 1, 3])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_4(self):
        # tc2 from gradescope algo1
        n = 10 
        W = 15
        heights = [32, 30, 19, 19, 17, 14, 10, 9, 8, 8]
        widths = [12, 5, 14, 15, 6, 7, 3, 1, 1, 3]

        expected_output = (6, 127, [1, 1, 1, 1, 2, 4])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_5(self):
        # t3 from gradescope algo1
        n = 5 
        W = 6
        heights = [13, 10, 8, 6, 3]
        widths = [3, 4, 1, 2, 6]

        expected_output = (4, 32, [1, 2, 1, 1])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_6(self):
        # t4 from gradescope algo1
        n = 20 
        W = 30
        heights = [43, 41, 40, 39, 36, 34, 32, 29, 27, 25, 23, 21, 19, 17, 16, 15, 14, 13, 12, 10]
        widths = [15, 17, 14, 4, 6, 4, 5, 14, 15, 16, 17, 14, 14, 14, 6, 7, 8, 5, 4, 3]

        expected_output = (10, 283, [1, 1, 4, 2, 1, 1, 1, 2, 3, 4])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_7(self):
        # t5 from gradescope algo1
        n = 10 
        W = 50
        heights = [54, 51, 48, 45, 29, 27, 25, 20, 4, 1]
        widths = [43, 13, 6, 35, 2, 1, 1, 1, 49, 1]

        expected_output = (4, 154, [1, 2, 5, 2])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_8(self):
        # t2 from gradescope algo2
        n = 10 
        W = 15
        heights = [31, 29, 25, 19, 4, 2, 4, 7, 8, 9]
        widths = [3, 4, 6, 5, 3, 1, 2, 14, 1, 3]

        expected_output = (4, 66, [3, 4, 1, 2])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_9(self):
        # t3 from gradescope algo2
        n = 5 
        W = 20
        heights = [9, 7, 3, 10, 11]
        widths = [4, 4, 4, 4, 15]

        expected_output = (2, 20, [3, 2])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_10(self):
        # t4 from gradescope algo2
        n = 20 
        W = 25
        heights = [65, 41, 31, 21, 11, 1, 2, 3, 3, 5, 6, 7, 8, 9, 13, 15, 17, 18, 19, 100]
        widths = [20, 2, 6, 12, 8, 4, 6, 7, 8, 1, 6, 7, 9, 8, 7, 8, 12, 16, 20, 5]

        expected_output = (8, 262, [2, 2, 4, 4, 3, 2, 1, 2])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_11(self):
        # t5 from gradescope algo2
        n = 10 
        W = 50
        heights = [8, 6, 4, 2, 1, 3, 5, 6, 7, 8]
        widths = [43, 36, 47, 4, 12, 15, 8, 1, 1, 9]

        expected_output = (4, 26, [1, 1, 1, 7])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    # custom tests start from here
    def testcase_12(self):
        n = 1
        W = 10
        heights = [15]
        widths = [9]

        expected_output = (1, 15, [1])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_13(self):
        n = 5
        W = 10
        heights = [15, 5, 10, 5, 20]
        widths = [2, 2, 2, 2, 2]

        expected_output = (1, 20, [5])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_14(self):
        n = 6
        W = 10
        heights = [35, 15, 15, 5, 10, 10]
        widths = [1, 2, 3, 4, 5, 5]

        expected_output = (2, 45, [4, 2])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_15(self):
        n = 6
        W = 10
        heights = [35, 15, 15, 5, 10, 10]
        widths = [1, 2, 3, 5, 4, 6]

        expected_output = (3, 50, [3, 1, 2])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_16(self):
        n = 5
        W = 10
        heights = [35, 15, 15, 5, 10]
        widths = [1, 2, 3, 5, 4]

        expected_output = (2, 45, [3, 2])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_17(self):
        n = 6
        W = 10
        heights = [35, 15, 15, 5, 10, 10]
        widths = [1, 2, 3, 5, 4, 7]

        expected_output = (3, 55, [3, 2, 1])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")
    
    def testcase_18(self):
        n = 6
        W = 10
        heights = [35, 15, 10, 5, 10, 15]
        widths = [3, 3, 2, 1, 1, 10]

        expected_output = (2, 50, [5, 1])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")

    def testcase_19(self):
        n = 4
        W = 2
        heights = [1, 2, 3, 4]
        widths = [2, 2, 2, 2]

        expected_output = (4, 10, [1, 1, 1, 1])

        output = program(n, W, heights, widths)

        self.assertEqual(output, expected_output, f"expected {expected_output} but received {output}")


if __name__ == "__main__":
    unittest.main()




