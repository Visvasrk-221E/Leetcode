#!/bin/python3

# Define the class
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "CD" : 400,
            "XL" : 40,
            "IV" : 4,
            "IX" : 9,
            "XC" : 90,
            "CM" : 900,
       }
        special = ["CD", "XL", "IV", "IX", "XC", "CM"]
        lom = []
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in special:
                lom.append(s[i:i+2])
                i += 2
            else:
                lom.append(s[i])
                i += 1
        for k in lom:
            total += map[k]
        return total

# Answers
engine = Solution()
roman_list = ['III', 'CDCXCM', 'XXIVX', 'LLLXLC', 'CMCMX', 'XXX','XXVII' ]
for x in roman_list:
	print(engine.romanToInt(x))

