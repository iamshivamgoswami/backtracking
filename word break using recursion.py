s = "leetcode"
dd = ["leet","code"]
d=set(tuple(dd))
def func(pos=0):
    if pos==len(s):
        return True
    for i in range(pos,len(s)):
        curr=s[pos:i+1]
        if curr in d and func(i+1):
            return True

    return False

print(func())