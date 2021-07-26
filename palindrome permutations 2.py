import collections


class Solution:
    def generatePalindromes(self, s: str) :

        c=collections.Counter(s)
        half="".join([k*(v//2) for k,v in c.items() ])

        half=[c for c in half]
        mid=[k for k,v in c.items() if v%2]
        if len(mid)>1:
            return []
        mid="" if len(mid)==0 else mid[0]

        ans=[]
        def func(tmp=[],counter=collections.Counter(half)):

            if len(tmp)==len(half):

                curr="".join(tmp)
                ans.append(curr+mid+curr[::-1])
                return
            else:

                for num in counter:
                    if counter[num] > 0:
                        tmp.append(num)
                        counter[num] -= 1
                        func(tmp, counter)
                        counter[num] += 1
                        tmp.pop()

        func()
        return ans

a=Solution()
print(a.generatePalindromes("aaa"))
