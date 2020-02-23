"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for i in range(n + 1)]
        idx = 0
        while idx ** 2 <= n:
            dp[idx ** 2] = 1
            idx += 1
        for idx in range(1, n + 1):
            iidx = 0
            while idx + iidx ** 2 <= n:
                dp[idx + iidx ** 2] = min(dp[idx] + 1, dp[idx + iidx ** 2])
                iidx += 1

        return int(dp[-1])


n = 12
solu = Solution()
print(solu.numSquares(n))


