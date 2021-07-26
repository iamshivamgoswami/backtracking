ans=[]
n=9
def func(row,diagonal,anti_diagonal,cols,tmp):
    if row==n:

        ans.append(tmp[:])
    for col in range(n):
        curr_diagonal=row-col
        cur_anti_diagonal=row+col
        if col in cols or cur_anti_diagonal in anti_diagonal or curr_diagonal in diagonal:
            continue
        cols.add(col)
        diagonal.add(curr_diagonal)
        anti_diagonal.add(cur_anti_diagonal)
        tmp.append(col)
        func(row+1,diagonal,anti_diagonal,cols,tmp)
        tmp.pop()
        cols.remove(col)
        diagonal.remove(curr_diagonal)
        anti_diagonal.remove(cur_anti_diagonal)

func(0,set(),set(),set(),[])
print(ans)
res=[]
for i in ans:
    l=[]
    for j in i:
        l.append(j*"."+"Q"+(n-j-1)*".")
    res.append(l)

print(res)

