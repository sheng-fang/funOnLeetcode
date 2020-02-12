class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        dp solution
        Args:
            s:

        Returns:

        """
        l = len(s)
        memo = [[0 for i in range(l)] for i in range(l)]
        max_l = 0
        max_str = ''

        for i in range(l):
            for j in range(i+1):
                if i - j <= 1 and s[i] == s[j]:
                    memo[i][j] = True
                    if i - j + 1 > max_l:
                        max_l = i - j + 1
                        max_str = s[j: i + 1]
                else:
                    if s[i] == s[j] and memo[i - 1][j + 1]:
                        memo[i][j] = True
                        if i - j + 1 > max_l:
                            max_l = i - j + 1
                            max_str = s[j: i + 1]
                    else:
                        memo[i][j] = False

        return max_str


    def longestPalindrome_bt(self, s: str) -> str:
        str_size = len(s)
        if str_size == 0:
            return ''
        max_palindromic = s[0]
        size_palindromic = 1
        for i in range(str_size):
            idx_low, idx_high = i, i
            while idx_low > 0 and idx_high < str_size - 1:
                idx_low -= 1
                idx_high += 1
                print("compare", s[idx_low: idx_high + 1])
                if s[idx_low] != s[idx_high]:
                    idx_low += 1
                    idx_high -= 1
                    break

            if (idx_high - idx_low + 1) > size_palindromic:
                size_palindromic = idx_high - idx_low + 1
                max_palindromic = s[idx_low: idx_high + 1]

            idx_low, idx_high = i, i + 1
            while True:
                if idx_low < 0 or idx_high >= str_size or s[idx_low] != s[idx_high]:
                    idx_low += 1
                    idx_high -= 1
                    break
                else:
                    idx_low -= 1
                    idx_high += 1

            if 2 * (i - idx_low + 1) > size_palindromic:
                size_palindromic = 2 * (i - idx_low + 1)
                max_palindromic = s[idx_low: idx_high + 1]

        return max_palindromic


if __name__ == '__main__':
    test = "cbbd"
    solu = Solution()
    print(solu.longestPalindrome(test))
