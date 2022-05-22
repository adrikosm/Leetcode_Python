"""
Given a string s, find the length of the longest substring
without repeating characters.

Ex.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3
"""


def lengthOfLongestSubstring(s) -> int:
    """
    Use hashmap in order to get both the value and
    the index
    """
    chars = {}
    start = 0
    max_length = 0

    for key, value in enumerate(s):
        if value in chars:
            start = max(start, chars[value] + 1)

        max_length = max(max_length, key - start + 1)
        chars[value] = key
    return max_length


def main():
    print(lengthOfLongestSubstring("abcabcbb"))  # EXPECTED 3


if __name__ == "__main__":
    main()
