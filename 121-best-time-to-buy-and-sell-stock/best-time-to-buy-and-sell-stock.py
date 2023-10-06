class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 0
        highest = 1
        maxProfit = 0
        length = len(prices)

        while lowest < length and highest < length:
            currentProfit = prices[highest]-prices[lowest]

            if currentProfit < 0 or highest == length-1:
                lowest += 1
                if lowest == highest:
                    highest += 1
            else:
                highest += 1

            maxProfit = max(maxProfit, currentProfit) 

        return 0 if maxProfit < 0 else maxProfit