# Leetcode 66

"""
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most
significant to least significant in left-to-right order. The large integer does
not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""


def plusOne(digits):
    # Initialize an empty string to build the full number
    num = ""

    # Convert each digit in the list to a string and concatenate to form the
    # full number as a string
    for digit in digits:
        digit = str(digit)
        num += digit

    num = int(num)

    num += 1

    # Convert the incremented number back into a list of digits
    num = list(map(int, str(num)))

    return num
