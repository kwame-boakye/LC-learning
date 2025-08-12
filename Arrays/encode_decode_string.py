"""
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.
Please implement encode and decode
Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]
Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]
"""


def encode(strs):
    res = ""

    for s in strs:
        res += str(len(s)) + "#" + s

    return res


def decode(s):
    res, i = [], 0

    while i < len(s):
        j = i

        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length

    return res
