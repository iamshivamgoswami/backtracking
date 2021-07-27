import collections
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def could_place(d, row, col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = "."

        def place_next_number(row, col):
            if col == 8 and row == 8:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:

                if col == 8:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == ".":
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)
                        if not sudoku_solved:
                            remove_number(d, row, col)

            else:
                place_next_number(row, col)

        def box_index(row, col):
            return (row // 3) * 3 + col // 3

        rows = [collections.defaultdict(int) for i in range(9)]
        cols = [collections.defaultdict(int) for i in range(9)]
        boxes = [collections.defaultdict(int) for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()