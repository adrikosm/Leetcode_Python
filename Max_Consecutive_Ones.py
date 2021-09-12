"""
Given a binary array nums,
return the maximum number of consecutive 1's in the array.
Example :
Input: nums = [1,1,0,1,1,1]
Output: 3

Explanation: The first two digits or the last three digits are
consecutive 1s.
The maximum number of consecutive 1s is 3

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
"""
from timeit import timeit


def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tmp = 0
    max_ones = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            tmp += 1
        else:
            tmp = 0
        if tmp > max_ones:
            max_ones = tmp

    return max_ones


def findMaxConsecutveOnes_Enchanced(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Uses less memory than simple
    # But takes a bit longer to compute
    result, local_max = 0, 0
    for n in nums:
        local_max = (local_max + 1 if n else 0)
        result = max(result, local_max)
    return result


def main():
    example_1 = [1, 1, 0, 1, 1, 1]
    example_2 = [0, 0, 1, 0, 1, 1]
    print(f"Answer for example 1: {findMaxConsecutiveOnes(example_1)}")
    print(f"Answer for example 2: {findMaxConsecutiveOnes(example_2)}")

    simple_time = timeit(lambda: findMaxConsecutiveOnes(example_1))
    enhanced_time = timeit(lambda: findMaxConsecutveOnes_Enchanced(example_1))
    print(f"{simple_time=:.02f} \n{enhanced_time=:0.2f}")


if __name__ == "__main__":
    main()
