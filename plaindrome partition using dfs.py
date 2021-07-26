s = "aabfjksgfiuwegfuiewfiuewhfui"
ans=[]
def func(pos,tmp=[],end=len(s)):
    if pos==end:
        ans.append(tmp[:])
    for  i in range(pos,end):
        curr=s[pos:i+1]
        if curr==curr[::-1]:
            tmp.append(curr)
            func(pos+1)
            tmp.pop()
func(0)
print(ans)