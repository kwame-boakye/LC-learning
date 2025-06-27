"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.

Example:
Input: x = 123
Output: 321
"""


def reverse(x):
    is_neg = False
    res = 0

    if x < 0:
        is_neg = True
        x *= -1

    while x > 0:
        res = (res * 10) + (x % 10)
        x //= 10

    if res < -(2**31) or res > 2**31 - 1:
        return 0

    return -res if is_neg else res
