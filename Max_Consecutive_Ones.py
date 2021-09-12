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


if __name__ == "__main__":
    example_1 = [1, 1, 0, 1, 1, 1]
    example_2 = [0, 0, 1, 0, 1, 1]
    print(f"Answer for example 1: {findMaxConsecutiveOnes(example_1)}")
    print(f"Answer for example 2: {findMaxConsecutiveOnes(example_2)}")
