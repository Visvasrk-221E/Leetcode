#!/bin/python3

# Define the class
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# Examples
engine = Solution()
xlist = [121, 131, 123, 124, 42124, 242, 678, 876, 10101]

for x in xlist:
	print(engine.isPalindrome(x))
