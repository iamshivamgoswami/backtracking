class Solution:
    def exist(self, board, word):
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                print(self.backtrack(row, col, word))
                if self.backtrack(row, col, word):
                    return True

        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True
        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.board[row][col] != suffix[0]:
            return False

        self.board[row][col] = "#"
        for x, y in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            ret = self.backtrack(x, y, suffix[1:])
            if ret:
                break
        self.board[row][col] = suffix[0]

        return ret