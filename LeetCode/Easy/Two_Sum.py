"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order
    Ex.
    nums = [2,7,11,15]
    target = 9
    Output = [0,1]
""" 

def two_sum(nums,target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                 return [required[target - nums[i]],i]
            else:
                required[nums[i]]=i

def main():
    print(two_sum([2,7,11,15], 9))


if __name__ == "__main__":
    main()
