#!/bin/python3

# Define the class
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index1, number1 in enumerate(nums):
            for index2, number2 in enumerate(nums):
                if number1 + number2 == target and index2 != index1:
                    return [index1, index2]

# Check Answer

engine=Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16]
targets = [5, 10, 15, 9, 7, 6, 5, 10, 20, 25, 30]
for target in targets:
	print(engine.twoSum(nums, target))

