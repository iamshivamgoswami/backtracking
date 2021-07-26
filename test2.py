import collections
class Solution:
    def combinationSum2(self, arr, target) :
        ans=[]
        c=collections.Counter(arr)
        c=[(k,v) for k,v in c.items()]
        def func(pos,summ=0,tmp=[]):
            if summ==target:
                    ans.append(sorted(tmp[:]))
            elif summ>target:
                return
            for i in range(pos,len(c)):
                curr_element,freq=c[i]
                if freq<=0:
                    continue
                tmp.append(curr_element)
                c[i]=(curr_element,freq-1)
                func(i,summ+curr_element)
                tmp.pop()
                c[i]=(curr_element,freq)



        func(0)
        return(ans)