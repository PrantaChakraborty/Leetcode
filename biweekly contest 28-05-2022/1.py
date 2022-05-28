"""
6083. Check if Number Has Equal Digit Count and Digit Value
"""


class Solution:
    def digitCount(self, num: str) -> bool:
        num_dict = {}
        arr = []
        for i in range(len(num)):
            num_dict[i] = 0
        for item in num:
            if int(item) in num_dict:
                num_dict[int(item)] += 1
        for i in range(len(num)):
            if int(num[i]) == num_dict[i]:
                arr.append(1)  # means True
            else:
                arr.append(0)  # means False
        if 0 in arr:
            return False
        else:
            return True




num = "1210"
# num = "130"
solution = Solution()
print(solution.digitCount(num))