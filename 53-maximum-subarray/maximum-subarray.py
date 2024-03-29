class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]
        length = len(nums)

        for i in range(1, length):
            currentSum = max(nums[i], currentSum + nums[i])

            maxSum = max(maxSum, currentSum)

        return maxSum