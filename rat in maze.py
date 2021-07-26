class Solution:
    def findPath(self, mat, n):
        ans = []
        if mat[0][0] == 0:
            return []
        if mat[-1][-1] == 0:
            return []

        def func(row, col, tmp=[]):
            if row == n - 1 and col == n - 1:
                ans.append(tmp[:])
            for i, j, d in [(row + 1, col, "D"), (row - 1, col, "U"), (row, col + 1, "R"), (row, col - 1, "L")]:
                if 0 <= i < n and 0 <= j < n and mat[i][j] == 1:
                    mat[row][col] = 0
                    tmp.append(d)
                    func(i, j, tmp)
                    mat[row][col] = 1
                    tmp.pop()

        func(0, 0)

        ans = sorted(["".join(i) for i in ans])
        return (ans)