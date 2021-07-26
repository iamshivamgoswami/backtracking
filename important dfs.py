


class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return
        self.rows = len(board)
        self.cols = len(board[0])
        border = []
        for i in range(self.rows):
            for j in range(self.cols):
                if i == 0:
                    border.append((i, j))
                if j == 0:
                    border.append((i, j))
                if i==self.rows-1:
                    border.append((i,j))
                if j==self.cols-1:
                    border.append((i,j))
        for row, col in border:
            self.dfs(board,row, col)

        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"

    def dfs(self,board, row, col):

        if board[row][col] != "O":
            return
        board[row][col] = "E"
        if col < self.cols - 1:
            self.dfs(board,row, col + 1)
        if row < self.rows - 1:
            self.dfs(board,row + 1, col)
        if row > 0:
            self.dfs(board,row - 1, col)
        if col > 0:
            self.dfs(board,row, col - 1)



