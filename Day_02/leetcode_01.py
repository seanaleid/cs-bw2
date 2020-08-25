# Title: Two Sum
# Source: https://leetcode.com/problems/two-sum/

# Instructions:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    result = list()
    for i,n in enumerate(nums):
        subN = target - n
        print(subN)
        if len(nums) == 2 and nums[0]+nums[1] == target:
            result.append(i)
        elif nums.count(subN) == 2:
            result.append(i)
        elif subN in nums and subN != n:
            idx = nums.index(subN)
            result.append(idx)
    sortedN = sorted(result)
    return sortedN


nums = [3,2,3]
target = 6
print(twoSum(nums, target))
