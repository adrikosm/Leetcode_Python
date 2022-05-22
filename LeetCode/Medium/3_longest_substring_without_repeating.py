"""
Given a string s, find the length of the longest substring
without repeating characters.

Ex.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3
"""


from numpy import char


def lengthOfLongestSubstring(s) -> int:
    """
    Use hashmap in order to get both the value and
    the index
    """
    chars = {}
    max_length = start = 0
    for key, value in enumerate(s):
        if value in chars and start <= chars[value]:
            start = chars[value]+1
        else:
            max_length = max(max_length, key - start+1)


def main():
    print(lengthOfLongestSubstring("abcabcbb"))  # EXPECTED 3


if __name__ == "__main__":
    main()
