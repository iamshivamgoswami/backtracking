import collections
nums=[1,1,2]
ans=[]
def func(pos, c=collections.Counter(nums), tmp=[]):

    if c is None:
        c = collections.Counter(nums)
    if pos==len(nums):
        ans.append(nums[:])
        return

    for i in range(pos,len(nums)):
        if c[nums[i]]<=0:
            continue
        c[nums[i]]-=1
        tmp.append(nums[i])
        func(i + 1, c, tmp)
        c[nums[i]]+=1


func(0)
print(ans)






