n=4
ans=[]
def backTrack(row,diagonals,anti_diagonal,cols):
    if row==n:
        ans.append([])
        return

    for col in range(n):
        curr_diagonal=row-col
        curr_anti_diagonal=row+col
        if (col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonal):
            continue
        cols.add(col)
        diagonals.add(curr_diagonal)
        anti_diagonal.add(curr_anti_diagonal)
        backTrack(row+1,diagonals,anti_diagonal,cols)
        cols.remove(col)
        diagonals.remove(curr_diagonal)
        anti_diagonal.remove(curr_anti_diagonal)

backTrack(0,set(),set(),set())
print(len(ans))
