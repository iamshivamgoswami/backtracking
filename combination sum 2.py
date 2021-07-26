import collections

arr=[10,1,2,7,6,1,5]
c=collections.Counter(arr)
c=[(a,c[a]) for a in c]

target=8
ans=[]
d=set()
def func(remain,curr,tmp):
    if remain==0:
        ans.append(tmp[:])
        return
    elif remain<0:
        return

    for i in range(curr,len(c)):
        print(c[i])
        curr_element,freq=c[i]
        if freq<=0:
            continue
        tmp.append(curr_element)
        c[i]=(curr_element,freq-1)
        func(remain-curr_element,i,tmp)
        tmp.pop()
        c[i]=(curr_element,freq)



func(target,0,[])

print(ans)
