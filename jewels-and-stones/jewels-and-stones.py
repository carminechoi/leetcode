class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewelsSet:
                count += 1

        return count