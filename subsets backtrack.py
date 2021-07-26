class Solution:
    def subsets(self, s: List[int]) -> List[List[int]]:
        ans = []

        def solve(pos, op=[]):
            ans.append(op[:])

            for i in range(pos, len(s)):
                op.append(s[i])
                solve(i + 1)
                op.pop()

        solve(0)
        return ans

