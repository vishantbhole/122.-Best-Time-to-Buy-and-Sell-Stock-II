#122. Best Time to Buy and Sell Stock II

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
if __name__ == "__main__":
    sol = Solution()
    
    prices = [7,1,5,3,6,4]
    print("Output is : ", sol.maxProfit(prices))
    
    prices2 = [1,2,3,4,5]
    print("Output is : ", sol.maxProfit(prices2))
