class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix[0])
        for i in range(length // 2 + length % 2):
            for j in range(length//2):
                tmp = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - j - 1]
                matrix[length - 1 - i][length - j - 1] = matrix[j][length - 1 -i]
                matrix[j][length - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp