"""
Given a string s, find the length of the longest substring without
duplicate characters.

"""

# 1. We define a function called lengthOfLongestSubstring that takes a string s as input.

# 2. Inside, we set max_len = 0 to store the maximum substring length found, and current = ""
# to represent the current substring we’re building without duplicates.

# 3. We loop through every character char in s.

# 4. If char already exists in current, that means we hit a duplicate. To fix this,
# we find the index of the duplicate character in current, and then reset current
# to drop everything up to and including that index (this way, the duplicate is
# removed and we continue with a clean substring).

# 5. After handling duplicates, we add the current character (char) to current.
# We then update max_len by comparing it with the length of current — keeping whichever is bigger.

# 6. Once the loop finishes, we return max_len, which represents the length of the
# longest substring without repeating characters.


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
