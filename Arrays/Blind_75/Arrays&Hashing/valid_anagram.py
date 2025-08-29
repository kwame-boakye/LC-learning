"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

"""

from collections import Counter


def ValidAnagram(s, t):
    if len(s) != len(t):
        return False

    w_1 = Counter(s)
    w_2 = Counter(t)

    for k, v in w_1.items():
        if w_1[k] != w_2[k]:
            return False

    return True
