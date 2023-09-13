class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def inBounds(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False
            return True
        
        nextState = [[0 for j in range(cols)] for i in range(rows)]
        for x in range(rows):
            for y in range(cols):
                live = 0
                if inBounds(x-1, y-1) and board[x-1][y-1] == 1:
                    live += 1
                if inBounds(x-1, y) and board[x-1][y] == 1:
                    live += 1
                if inBounds(x-1, y+1) and board[x-1][y+1] == 1:
                    live += 1
                if inBounds(x, y-1) and board[x][y-1] == 1:
                    live += 1
                if inBounds(x, y+1) and board[x][y+1] == 1:
                    live += 1
                if inBounds(x+1, y-1) and board[x+1][y-1] == 1:
                    live += 1
                if inBounds(x+1, y) and board[x+1][y] == 1:
                    live += 1
                if inBounds(x+1, y+1) and board[x+1][y+1] == 1:
                    live += 1

                if live < 2 or live > 3:
                    nextState[x][y] = 0
                elif live == 3:
                    nextState[x][y] = 1
                else:
                    nextState[x][y] = board[x][y]
                    
        for i in range(rows):
            for j in range(cols):
                board[i][j] = nextState[i][j]                
