"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum
of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid: list):
        m = len(grid)
        if m == 0:
            raise Exception("Empty input!")
        n = len(grid[0])

        dp = [[float('inf') for i in range(n+1)] for i in range(m+1)]
        dp[0][1], dp[1][0] = 0, 0

        for idx_m in range(0, m):
            for idx_n in range(0, n):
                dp[idx_m + 1][idx_n + 1] = min(dp[idx_m][idx_n + 1], dp[idx_m + 1][idx_n]) + grid[idx_m][idx_n]

        return dp[m][n]


    def maxPathSum(self, grid: list):
        m = len(grid)
        if m == 0:
            raise Exception("Empty input!")
        n = len(grid[0])

        dp = [[-float('inf') for i in range(n+1)] for i in range(m+1)]
        dp[0][1], dp[1][0] = 0, 0

        for idx_m in range(0, m):
            for idx_n in range(0, n):
                dp[idx_m + 1][idx_n + 1] = max(dp[idx_m][idx_n + 1], dp[idx_m + 1][idx_n]) + grid[idx_m][idx_n]

        return dp[m][n]


test = [[1,3,1],[1,5,1],[4,2,1]]
solu = Solution()

print(solu.minPathSum(test))
print(solu.maxPathSum(test))
