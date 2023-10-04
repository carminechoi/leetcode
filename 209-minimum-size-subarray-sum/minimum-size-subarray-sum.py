class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        subSum = nums[0]
        smallestLength = len(nums) + 1

        while right < len(nums):
            if subSum < target:
                right += 1
                if right < len(nums):
                    subSum += nums[right]
            elif subSum >= target:
                smallestLength = min(smallestLength, right-left+1)
                subSum -= nums[left]
                left += 1

        return 0 if smallestLength == len(nums) + 1 else smallestLength

        