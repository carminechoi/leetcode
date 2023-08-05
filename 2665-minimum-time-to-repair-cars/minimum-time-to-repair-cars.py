class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepair(minutes):
            numberOfCars = 0

            for rank in ranks:
                numberOfCars += math.floor(math.sqrt(minutes // rank))

            return numberOfCars >= cars

        left = 1
        right = max(ranks) * cars *cars

        while left < right:
            mid = left + (right - left) // 2
            if canRepair(mid):
                right = mid
            else:
                left = mid + 1
            
        return right
