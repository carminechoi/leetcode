class SmallestInfiniteSet:

    def __init__(self):
        self.excluded = set()
        self.minValue = 1

    def popSmallest(self) -> int:
        smallest = self.minValue
        
        self.minValue += 1
        while self.minValue in self.excluded:
            self.minValue += 1

        self.excluded.add(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.excluded:
            self.excluded.remove(num)
            self.minValue = min(self.minValue, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)