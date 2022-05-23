"""
linK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr_len = len(prices)
        left = 0
        right = 1
        total_profit = 0
        while right < arr_len:
            current_profit = prices[right] - prices[left]
            if current_profit > 0:
                # when current profit is a positive number
                total_profit += current_profit
                left = right
            else:
                left = right
            right += 1
        return total_profit











prices = [7,6,4,3,1] # 0
# prices = [1, 2, 3, 4, 5] #  4

# prices = [7,1,5,3,6,4] # 7
solution = Solution()
print(solution.maxProfit(prices))
