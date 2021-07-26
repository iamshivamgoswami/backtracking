class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def func(i=0, j=0):
            key = (i, j)
            if key in memo:
                return memo[key]
            if j == len(p):
                ans = i == len(s)
            elif i == len(s):
                ans = j == len(p) or all(x == "*" for x in p[:j+1])

            else:
                first_match = p[j] in {s[i], ".", "*"}
                if p[j] == "*":
                    ans = func(i + 1, j) or func(i, j + 1)
                else:
                    ans = first_match and func(i + 1, j + 1)

            memo[key] = ans
            return ans

        return func()