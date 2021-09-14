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


def sorted_squares_simple(nums):
    start = time.time()
    sorted_list = []
    for i in nums:
        sorted_list.append(i * i)
    sorted(sorted_list)
    end = time.time()
    return sorted_list, end - start


def sorted_squares_second(nums):
    start = time.time()
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    end = time.time()
    sorted(nums)
    return nums, end - start


def sortedSquares(nums):
    start = time.time()
    res = sorted([n * n for n in nums])
    end = time.time()
    return res, end - start


def main():
    nums = [-4, -1, 0, 3, 10]
    sorted_1, time_1 = sorted_squares_simple(nums)
    sorted_2, time_2 = sorted_squares_second(nums)
    sorted_3, time_3 = sortedSquares(nums)

    print(f"Sorted 1 {sorted_1}")
    print(f"Sorted 2 {sorted_2}")
    print(f"Sorted 3 {sorted_3}")
    print(f"Time of 1 {time_1:0.9f}")
    print(f"Time of 2 {time_2:0.9f}")
    print(f"Time of 3 {time_3:0.9f}")


if __name__ == "__main__":
    main()
