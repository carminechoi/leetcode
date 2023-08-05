class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(mid):
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / mid)
            
            return totalHours <= h

        left = 1
        right = max(piles)

        while left < right: 
            mid = left + (right - left) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1

        return right