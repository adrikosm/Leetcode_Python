"""
Given an array nums of integers, return how 
many of them contain an even number of digits. 

Example 1

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain 
an even number of digits

"""
from timeit import timeit


def find_numbers(nums):
    total = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            total += 1

    return total


def main():
    nums = [12, 345, 2, 6, 7896]
    solution_1_time = timeit(lambda: find_numbers(nums))
    print(find_numbers(nums))
    print(f"{solution_1_time=:0.2f}s")


if __name__ == "__main__":
    main()
