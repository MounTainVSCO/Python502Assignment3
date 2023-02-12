##
# Student Name: William Zhao
# Course: CIS 502 Applied Python Programming
# Lab # 3 - Algorithms Using Conditional Execution and Looping Constructs
# Application: Generating Mathematical Sequences
# Description: Compute a hailstone sequence of 'length' steps beginning with a given
#              'start' value.  Validate that the start value is a positive integer. 
# Version: Python 3.8
# Solution File: WilliamZhaoLab3.py
# Date: 02/11/23
##

# Program Source


def hailstone_min_max(l):
    """
    finds the maximum and minimum 
    value of the hailstone sequence
    """
    
    return min(l), max(l)

def validate_start():
    """
    Continuously ask for user input until a 
    valid non-negative number is entered
    """

    while True:
        try:
            starting_num = int(input("Enter a non-negative starting number: "))
            if starting_num >= 0:
                return starting_num
        except ValueError:
            print("Invalid Input")

def validate_len():
    """
    Continuously ask for user input until a 
    valid non-negative sequence length is entered
    """

    while True:
        try:
            num = int(input("Enter the amount of hailstone sequences: "))
            if num > 0:
                return num
        except ValueError:
            print("Invalid Input")
            

def hailstone_seq(start, length, seq=None):
    """
    Computes the hailstone sequence 
    of a given length, starting from a given number
    """
    if seq is None: # Resets the list everytime function is called
        seq = []    # multiple times
    seq.append(int(start))
    if length == 1:
        return seq
    if start % 2 == 1:
        start = ((3*start)+1)
    else:
        start = start/2
    return hailstone_seq(start, length - 1, seq)

def main():
    start_num = validate_start()
    length = validate_len()
    list_seq = hailstone_seq(start_num, length)
    min_value, max_value = hailstone_min_max(list_seq)
    print("The hailstone sequence is:", list_seq)
    print("The minimum value in the sequence is:", min_value)
    print("The maximum value in the sequence is:", max_value)

if __name__ == "__main__":
    main()

'''
Enter a non-negative starting number: 7
Enter the amount of hailstone sequences: 10
The hailstone sequence is: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20]
The minimum value in the sequence is: 7
The maximum value in the sequence is: 52
'''

'''
Enter a non-negative starting number: 7
Enter the amount of hailstone sequences: 20
The hailstone sequence is: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1]
The minimum value in the sequence is: 1
The maximum value in the sequence is: 52
'''