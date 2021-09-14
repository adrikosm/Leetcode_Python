"""
Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

"""
import timeit


def sorted_squares_simple(nums):
    sorted_list = []
    for i in nums:
        sorted_list.append(i * i)
    return sorted(sorted_list)


def sortedSquares(nums):
    res = sorted([n * n for n in nums])
    return res


def sorted_squares_second(nums):
    for i in range(len(nums)):
        nums[i] = abs(nums[i]) ** 2
    nums.sort()
    return nums


def main():
    nums = [-4, -1, 0, 3, 10]
    # print(sorted_squares_simple(nums))
    # print(sortedSquares(nums))
    # print(sorted_squares_second(nums))
    sorted_first = timeit.timeit(lambda: sorted_squares_simple(nums), number=12)
    sorted_second = timeit.timeit(lambda: sortedSquares(nums), number=12)
    sorted_third = timeit.timeit(lambda: sorted_squares_second(nums), number=12)
    print(f"{sorted_first:0.8f}")
    print(f"{sorted_second:0.8f}")
    print(f"{sorted_third:0.8f}")


if __name__ == "__main__":
    main()
