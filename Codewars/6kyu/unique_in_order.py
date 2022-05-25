"""
Implement the function unique_in_order which takes as 
argument a sequence and returns a list of items without any 
elements with the same value next to each other and preserving 
the original order of elements.
Ex.

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
"""


from urllib3 import Retry


def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    return result


def unique_in_order_second(iterable):
    chars = []
    for i in range(len(iterable)):
        if i == 0 or iterable[i] != iterable[i-1]:
            chars.append(iterable[i])
    return chars


def main():
    print(unique_in_order('AAAABBBCCDAABBB'))
    print(unique_in_order([1, 2, 3, 3, 4, 4, 4, 1]))  # EXPECTED [1,2,3,4,1]
    print(unique_in_order_second('AAAABBBCCDAABBB'))
    print(unique_in_order_second([1, 2, 3, 3, 4, 4, 4, 1]))


if __name__ == "__main__":
    main()
