"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""

class Solution:
    def isMatch(self, s: str, p: str):
        assert isinstance(s, str)
        assert isinstance(p, str)

        s_len = len(s)
        p_len = len(p)

        memo = [[False for i in range(p_len + 1)] for i in range(s_len + 1)]
        memo[-1][-1] = True

        for i in range(s_len, -1, -1):
            for j in range(p_len - 1, -1, -1):
                first_match = i < s_len and p[j] in [s[i], '.']

                if j + 1 < p_len and p[j+1] == '*':
                    memo[i][j] = memo[i][j + 2] or first_match and memo[i+1][j]
                else:
                    memo[i][j] = first_match and memo[i+1][j+1]

        return memo[0][0]

s = 'aa'
p = 'a*'

solu = Solution()
print(solu.isMatch(s, p))
