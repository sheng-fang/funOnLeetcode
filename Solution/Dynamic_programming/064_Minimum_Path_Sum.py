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

        dp = [0 for i in range(n)]
        dp_rt = [[] for i in range(n)]

        for idx_m in range(0, m):
            for idx_n in range(0, n):
                if idx_m == 0 and idx_n == 0:
                    dp[0] = grid[idx_m][idx_n]
                    dp_rt[0].append(idx_m * n + idx_n)
                elif idx_m == 0:
                    dp[idx_n] = dp[idx_n - 1] + grid[idx_m][idx_n]
                    dp_rt[idx_n] = dp_rt[idx_n - 1] + [idx_m * n + idx_n]
                elif idx_n == 0:
                    dp[0] = dp[0] + grid[idx_m][idx_n]
                    dp_rt[idx_n] = dp_rt[idx_n] + [idx_m * n + idx_n]
                else:
                    if dp[idx_n] > dp[idx_n - 1]:
                        dp[idx_n] = dp[idx_n - 1] + grid[idx_m][idx_n]
                        dp_rt[idx_n] = dp_rt[idx_n - 1] + [idx_m * n + idx_n]
                    else:
                        dp[idx_n] = dp[idx_n] + grid[idx_m][idx_n]
                        dp_rt[idx_n] = dp_rt[idx_n] + [idx_m * n + idx_n]

        return dp[n - 1]


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
