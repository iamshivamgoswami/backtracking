import collections
class Solution(object):
    def generatePalindromes(self, s):
        counter = collections.Counter(s)
        ans = []
        mid = [k for k, v in counter.items() if v % 2]

        if len(mid) > 1:
            return[]
        mid = "" if mid == [] else mid[0]
        half = "".join([k * (v // 2) for k, v in counter.items()])
        half = [c for c in half]
        ans = []

        def func(pos, n, d=set()):
            if pos == n:
                if tuple(half) not in d:
                    d.add(tuple(half))
                    ans.append("".join(half) + mid + "".join(half[::-1]))
            else:
                for i in range(pos, n):
                    half[i], half[pos] = half[pos], half[i]
                    func(pos + 1, n, d)
                    half[i], half[pos] = half[pos], half[i]

        func(0, len(half))

        return (ans)

