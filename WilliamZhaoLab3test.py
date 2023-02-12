##
# Student Name: William Zhao
# Course: CIS 502 Applied Python Programming
# Application: Test Driver
# Description: Test Driver for hailstone sequence and min and max
# Version: Python 3.8
# Solution File: WilliamZhaoTesterLab3.py
# Date: 02/11/23
##

# Program Source
import unittest
import assignment3 as as3


class TestHailstoneSequence(unittest.TestCase):
    def test_case1(self):
        '''
        test function for
        start: 7, sequence length: 10
        '''

        start = 7
        length = 10
        expected_seq = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20]
        seq = as3.hailstone_seq(start, length)
        min_value, max_value = as3.hailstone_min_max(seq)
        self.assertEqual(seq, expected_seq, f"Failed Test Case 1: expected {expected_seq} but got {seq}")
        self.assertEqual(min_value, 7, f"Failed Test Case 1: expected minimum value to be 1 but got {min_value}")
        self.assertEqual(max_value, 52, f"Failed Test Case 1: expected maximum value to be 52 but got {max_value}")

        print(f'''
            #Test Case 1:

            The hailstone sequence is: {seq}
            The minimum value in the sequence is: {max_value}
            The minimum value in the sequence is: {min_value}
        '''
        )

    def test_case2(self):
        '''
        test function for
        start: 7, sequence length: 20
        '''

        start = 7
        length = 20
        expected_seq = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1]
        seq = as3.hailstone_seq(start, length)
        min_value, max_value = as3.hailstone_min_max(seq)
        self.assertEqual(seq, expected_seq, f"Failed Test Case 2: expected {expected_seq} but got {seq}")
        self.assertEqual(min_value, 1, f"Failed Test Case 2: expected minimum value to be 1 but got {min_value}")
        self.assertEqual(max_value, 52, f"Failed Test Case 2: expected maximum value to be 52 but got {max_value}")

        print(f'''
            #Test Case 2:

            The hailstone sequence is: {seq}
            The minimum value in the sequence is: {max_value}
            The minimum value in the sequence is: {min_value}
        '''
        )


if __name__ == "__main__":
    unittest.main()


'''
#Test Case 1:

The hailstone sequence is: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20]
The minimum value in the sequence is: 52
The minimum value in the sequence is: 7


#Test Case 2:

The hailstone sequence is: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1]
The minimum value in the sequence is: 52
The minimum value in the sequence is: 1
'''
