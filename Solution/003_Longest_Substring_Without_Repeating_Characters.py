"""
Given a string, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        assert isinstance(s, str)

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        rec = dict()
        max_len = 0
        head = 0
        for idx, ltr in enumerate(s):
            if ltr in rec:
                curr_len = idx - head
                head = rec[ltr] + 1 if rec[ltr] + 1 > head else head
                if curr_len > max_len:
                    max_len = curr_len

            rec[ltr] = idx

        curr_len = len(s) - head
        max_len = curr_len if curr_len > max_len else max_len

        return max_len



test_str = "abba"
solu = Solution()
print(solu.lengthOfLongestSubstring(test_str))
