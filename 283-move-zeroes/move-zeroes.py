class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # j = 0
        # for i in range(0, len(nums)):
        #     if nums[j] == 0:
        #         nums.pop(j)
        #         nums.append(0)
        #     else:
        #         j += 1

        i = j = 0
        
        while i < len(nums):
            while j < len(nums) and nums[j] == 0: 
                j += 1

            if j >= len(nums):
                break
            
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j += 1

