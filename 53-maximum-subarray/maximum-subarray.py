class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEnd = 0
        maxSoFar = nums[0]

        for num in nums:
            maxEnd = max(num, maxEnd + num)
            maxSoFar = max(maxSoFar, maxEnd)

        return maxSoFar