import collections


class Solution:
    def permuteUnique(self,nums):
        ans=[]
        def func(tmp=[],counter=collections.Counter(nums)):
            if len(tmp)==len(nums):
                ans.append(tmp[:])
                return

            for num in counter:
                if counter[num]>0:
                    tmp.append(num)
                    counter[num]-=1
                    func(tmp,counter)
                    tmp.pop()
                    counter[num]+=1
        func()
        return ans
