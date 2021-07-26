s = "pineapplepenapple"

d=["apple","pen","applepen","pine","pineapple"]
d=set(tuple(d))
ans=[]
def func(pos,n=len(s),tmp=[]):
    if len("".join(tmp[:]))==len(s):
        ans.append(" ".join(tmp[:]))
    for i in range(pos,n):
        if s[pos:i+1] in d:
            arr=s[pos:i+1]
            tmp.append(arr)
            func(i+1)
            tmp.pop()
func(0)
print(ans)

