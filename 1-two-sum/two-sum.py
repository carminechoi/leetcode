class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ps = {}
        
        for i in range(0, len(nums)):
            if nums[i] in ps:
                return [i, ps[nums[i]]]
            else:
                ps[target - nums[i]] = i

        return []