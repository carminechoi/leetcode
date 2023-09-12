class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        i = 1
        for j in range(1, size):
            if nums[j-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i