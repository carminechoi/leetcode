class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findTarget():
            # Find any target index using binary search
            left, right = 0, len(nums)

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            
            # If target not found
            return -1

        if not nums:
            return [-1, -1]
        
        index = findTarget()

        start, end = index, index
        if index == -1:
            return [-1, -1]

        # Find start
        while start >= 0 and nums[start] == target:
            start -= 1
                
        # Find end
        while end < len(nums) and nums[end] == target:
            end += 1

        return [start+1, end-1]