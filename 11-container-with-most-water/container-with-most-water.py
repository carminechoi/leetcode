class Solution:
    def maxArea(self, heightList: List[int]) -> int:
        left, right = 0, len(heightList) - 1
        result = 0

        while left < right:
            width = right - left
            height = min(heightList[left], heightList[right])
            result = max(result, width * height)

            if heightList[left] > heightList[right]:
                right -= 1
            else:
                left += 1

        return result
