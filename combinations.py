class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        ans = []

        def func(pos=0, tmp=[]):
            if len(tmp) == k:
                ans.append(tmp[:])

            for i in range(pos, len(nums)):
                tmp.append(nums[i])
                func(i + 1, tmp)
                tmp.pop()

        func()
        return ans