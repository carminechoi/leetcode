class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        fp = sp = 0

        while fp < len(firstList) and sp < len(secondList):
            start = max(firstList[fp][0], secondList[sp][0])
            end = min(firstList[fp][1], secondList[sp][1])

            if start <= end:
                intersections.append([start, end])

            if firstList[fp][1] < secondList[sp][1]:
                fp += 1
            else:
                sp += 1

        return intersections