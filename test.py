class Solution:
    def isValidPalindrome(self, a: str, k: int) -> bool:
        b = a[::-1]
        n = len(a)

        dp = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(a) - dp[-1][-1]==k
