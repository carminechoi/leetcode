class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # brute force
        # time: O(n * k)
        # space: O(1)
        # for i in range(k):
        #     temp = nums.pop()
        #     nums.insert(0, temp)

        def reverse(start, end):
            while start < end:
                nums[start] , nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        # small optimization
        length = len(nums)
        k = k % length

        reverse(0, length-1)
        reverse(0, k - 1)
        reverse(k, length-1)

        

        

