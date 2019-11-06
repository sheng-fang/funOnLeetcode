class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0:
            if len(p) >= 2 and p[1] == '*':
                return True
            else:
                return False

        if len(p) == 0:
            return False

        for idx in range(len(s)):
