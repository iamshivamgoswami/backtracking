class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:

        ans = []

        def func(pos, rem=target, tmp=[]):
            if rem == 0:
                ans.append(tmp[:])
            elif rem < 0:
                return

            for i in range(pos, len(arr)):
                tmp.append(arr[i])
                func(i, rem - arr[i], tmp)
                tmp.pop()

        func(0)
        return (ans)

