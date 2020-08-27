# Title:  Search in Rotated Sorted Array
# Source: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Instructions:
# Given an integer array nums sorted in ascending order, and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You should search for target in nums and if you found return its index, otherwise return -1.

# Example:

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# Notes:
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4

def search(nums, target):
    result = -1
    for n in nums:
        if n == target:
            result = nums.index(n)
    return result

nums = [4,5,6,7,0,1,2]
target = 1

print(search(nums, target))