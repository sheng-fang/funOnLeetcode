"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)

        if m == 0:
            raise Exception("Empty input!")

        n = len(obstacleGrid[0])

        pd = [0 for i in range(n)]

        for idx_m in range(m):
            for idx_n in range(n):
                if obstacleGrid[idx_m][idx_n] == 1:
                    pd[idx_n] = 0
                else:
                    if idx_m == 0 and idx_n == 0:
                        pd[idx_n] = 1
                    elif idx_m == 0:
                        pd[idx_n] = pd[idx_n - 1]
                    elif idx_n == 0:
                        continue
                    else:
                        pd[idx_n] = pd[idx_n - 1] + pd[idx_n]

        return pd[-1]

test = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

solu = Solution()
print(solu.uniquePathsWithObstacles(test))