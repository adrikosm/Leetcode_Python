"""
Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

"""
import time
import timeit


def another_try(nums):
    result = sorted([n * n for n in nums])
    return result


def main():
    nums = [-4, -1, 0, 3, 10]
    sorted_4 = another_try(nums)

    print(f"Original Array{nums}")
    print(f"Expected output: [0,1,9,16,100]\n")
    print(f"Sorted try {sorted_4}")


if __name__ == "__main__":
    main()
