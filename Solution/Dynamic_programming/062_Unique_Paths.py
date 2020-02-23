"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pd = [0 for i in range(n)]

        for idx_m in range(m):
            for idx_n in range(n):
                if idx_m == 0 and idx_n == 0:
                    pd[idx_n] = 1
                elif idx_m == 0:
                    pd[idx_n] = pd[idx_n - 1]
                elif idx_n == 0:
                    continue
                else:
                    pd[idx_n] = pd[idx_n - 1] + pd[idx_n]

        return pd[-1]


m = 2
n = 3

solu = Solution()
print(solu.uniquePaths(m,n))