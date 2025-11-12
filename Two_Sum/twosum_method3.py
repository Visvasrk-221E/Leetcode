#!/bin/python3

# Define the class
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

# Check Answer

engine=Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16]
targets = [5, 10, 15, 9, 7, 6, 5, 10, 20, 25, 30]
for target in targets:
	print(engine.twoSum(nums, target))

