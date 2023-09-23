class Solution:
    def average(self, salarys: List[int]) -> float:
        minimum = float(inf)
        maximum = 0
        total = 0

        for salary in salarys:
            minimum = min(minimum, salary)
            maximum = max(maximum, salary)

            total += salary

        total = total - minimum - maximum

        average = total / (len(salarys) - 2)

        return average