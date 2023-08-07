class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        left, right = 0, len(matrix) - 1

        while left <= right:
            row = left + (right - left) // 2

            if target >= matrix[row][0] and target <= matrix[row][-1]:
                # search row
                left, right = 0, len(matrix[row]) - 1 

                while left <= right:
                    mid = left + (right - left) // 2

                    if target == matrix[row][mid]:
                        return True
                    elif target < matrix[row][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False

            elif target < matrix[row][0]:
                right = row - 1
            else:
                left = row + 1
            
        return False