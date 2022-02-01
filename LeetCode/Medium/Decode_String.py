"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside
the square brackets is being repeated exactly k times. Note that k is
guaranteed to be a positive integer.
You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data
does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].
   Ex.
    Input: s = "3[a]2[bc]" (string)
    Output: "aaabcbc"      (string)
"""

def decode_string(s):
    stack = []
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
    else:
        substring = ""
        while stack[-1] != "[":
            substring = stack.pop() + substring
        stack.pop()
        mul = ""
        while stack and stack[-1].isdigit():
            mul = stack.pop() + mul
        stack.append(int(mul) * substring)

    return "".join(stack)


def decodeString(s):
    stack, num, string = [], 0, ""
    for element in s:
        if element == "[":
            stack += string,
            stack += num,
            num, string = 0, ""
        elif element == "]":
            pre_num, pre_string = stack.pop(), stack.pop()
            string = pre_string + pre_num * string
        elif element.isdigit():
            num = num * 10 + int(element)
        else:
            string += element
    return string


def main():
    print(decodeString("3[a]2[bc]"))  # Expected: aaabcbc
    print(decodeString("2[b]2[c]1[d]"))  # Expected: bbccd
    print(decodeString("3[a2[c]]"))  # Expecte: accaccacc
    print(decodeString("2[abc]3[cd]ef"))  # Expected: abcabccdcdcdef


if __name__ == "__main__":
    main()
