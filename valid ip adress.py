class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def func(start, n=len(s), tmp=[]):
            if len(tmp) == 4:
                if start == n:
                    ans.append(".".join(tmp[:]))
                return

            for i in range(start, min(start + 3, n)):
                if s[start] == "0" and i > start:
                    continue
                if 0 <= int(s[start:i + 1]) <= 255:
                    tmp.append(s[start:i + 1])
                    func(i + 1)
                    tmp.pop()

        func(0)
        return ans