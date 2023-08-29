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

        # i = j = 0
        
        # while i < len(nums):
        #     while j < len(nums) and nums[j] == 0: 
        #         j += 1

        #     if j >= len(nums):
        #         break
            
        #     if nums[i] == 0:
        #         nums[i], nums[j] = nums[j], nums[i]

        #     i += 1
        #     j += 1

        index = 0  
       
        for i in range(len(nums)):
            if nums[i] != 0:
                # If the current element is non-zero, swap it with the element at index
                # This effectively moves non-zero elements to the beginning of the list
                nums[i], nums[index] = nums[index], nums[i]
                index += 1 

        
        # 0 1 0 3 12
        # 1 0 0 3 12
        # 1 3 0 0 12
        # 1 3 12 0 0

        # time: O(n)
        # space: O(1)

