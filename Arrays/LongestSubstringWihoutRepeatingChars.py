"""
Given a string s, find the length of the longest substring without
duplicate characters.

"""


def lengthOfLongestSubstring(s):
    max_len = 0
    current = ""

    for char in s:
        if char in current:
            index = current.index(char)
            current = current[index + 1 :]
        current += char
        max_len = max(max_len, len(current))

    return max_len
