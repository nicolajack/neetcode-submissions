class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bprofit = 0
        curMin = prices[0]
        for i in range(len(prices)):
            if prices[i] - curMin > bprofit:
                bprofit = prices[i] - curMin
            if prices[i] < curMin:
                curMin = prices[i]

        return bprofit
