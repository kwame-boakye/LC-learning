# Leetcode 2 Add two numbers

"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers
and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.


Sample Input:
# l1 = [2,4,3], l2 = [5,6,4]
# Sample Output:
# [7,0,8]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
