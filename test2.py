class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        ans = []

        def solve(pos, op=[]):
            if len(op)==k:

                ans.append(op[:])

            for i in range(pos, len(s)):
                op.append(nums[i])
                solve(i + 1)
                op.pop()

        solve(0)
        return ans

