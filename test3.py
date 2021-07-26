class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [i for i in range(1, 10)]
        c=[(i,1) for i in range(1,10)]
        ans=[]
        target = n
        def func(pos=0,summ=0,tmp=[]):
            if len(tmp)==k and summ==target:
                ans.append(tmp[:])
            if summ>target:
                return
            if len(tmp)>k:
                return
            for i in range(pos,len(arr)):
                curr_element,freq=c[i]
                if freq<=0:
                    continue
                tmp.append(arr[i])
                c[i]=(curr_element,freq-1)
                func(i,summ+curr_element,tmp)
                tmp.pop()
                c[i]=(curr_element,freq)

        func()
        return ans
