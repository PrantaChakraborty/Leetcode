"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict1 = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        roman_dict2 = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        result1 = 0
        result2 = 0
        sub_string_arr = []
        # separate the values from s to another array if s contains key form roman_dict2
        for item in roman_dict2.keys():
            if item in s:
                sub_string_arr.append(item)
                s = s.replace(item, "")
        if len(sub_string_arr) > 0:
            for item in roman_dict2:
                if item in sub_string_arr:
                    result2 += roman_dict2[item]
        if len(s) > 0:
            for item in s:
                if item in roman_dict1:
                    result1 += roman_dict1[item]
        return result1 + result2


s = "MMMXLV"
solution = Solution()
print(solution.romanToInt(s))
