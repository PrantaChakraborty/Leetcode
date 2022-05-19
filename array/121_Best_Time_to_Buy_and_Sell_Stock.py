"""
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr_len = len(prices)
        left = 0
        right = 1
        max_profit = 0
        while right < arr_len:
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit





prices = [3,2,6,5,0,3]
solution = Solution()
print(solution.maxProfit(prices))
