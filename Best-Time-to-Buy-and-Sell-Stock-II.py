class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_price = prices[0]
        for p in range(1, len(prices)):
            curr_price = min(curr_price, prices[p])
            if curr_price < prices[p]:
                res += (prices[p] - curr_price)
                curr_price = prices[p]
                
        return res
            
        