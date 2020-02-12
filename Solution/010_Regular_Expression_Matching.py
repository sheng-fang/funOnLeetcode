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

        if s_len == 0 and p_len == 0:
            return True

        if s_len == 0 and p_len != 0:
            return self.is_all_star(p)

        if s_len != 0 and p_len == 0:
            return False

        c_list = []
        tmp_str = ''
        for idx in range(s_len - 1):
            if s[idx] != s[idx + 1]:
                c_list.append()



    @staticmethod
    def is_all_star(my_str):
        for c in my_str:
            if c is '*':
                continue
            else:
                return False

        return True

