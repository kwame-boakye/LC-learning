"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a fixed
font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

"""


def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [""] * numRows
    index, step = 0, 1

    for char in s:
        rows[index] += char

        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1

        index += step

    return "".join(rows)
