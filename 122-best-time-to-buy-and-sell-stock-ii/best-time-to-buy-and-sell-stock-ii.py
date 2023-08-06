class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        profit = 0
        total = 0

        for price in prices:
            profit = price - minPrice
            if profit > 0:
                total += profit
                minPrice = price
            else:
                minPrice = min(minPrice, price)
        
        return total