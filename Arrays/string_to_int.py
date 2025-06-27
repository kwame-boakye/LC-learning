"""

Implement the myAtoi(string s) function, which converts a string to a
32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+',
assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit
character is encountered or the end of the string is reached. If no digits
were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range
[-231, 231 - 1], then round the integer to remain in the range. Specifically,
integers less than -231 should be rounded to -231, and integers greater
than 231 - 1 should be rounded to 231 - 1.
Input: s = "42"

Output: 42

Explanation:
The underlined characters are what is read in and the caret
is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)

"""


def myAtoi(s):
    s = s.lstrip()
    i = 0
    sign = 1
    parsed = 0

    if not s:
        return 0

    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        i += 1
        sign = -1

    while i < len(s):
        cur = s[i]

        if not cur.isdigit():
            break
        else:
            parsed = (parsed * 10) + int(cur)

        i += 1

    parsed *= sign

    if parsed < -(2**31):
        return -(2**31)
    elif parsed > 2**31 - 1:
        return 2**31 - 1
    else:
        return parsed
