"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row
below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
class Solution:
    def minimumTotal(self, triangle) -> int:
        m = len(triangle)

        if m == 0:
            raise Exception("Empty input!")

        n = len(triangle[m - 1])

        dp = [[float('inf') for j in range(i+1)] for i in range(n)]

        for idx_m in range(m):
            for idx_n in range(idx_m + 1):
                if idx_m == 0 and idx_n == 0:
                    dp[idx_m][idx_n] = triangle[idx_m][idx_n]
                elif idx_n == 0:
                    dp[idx_m][idx_n] = dp[idx_m - 1][idx_n] + triangle[idx_m][idx_n]
                elif idx_n == idx_m:
                    dp[idx_m][idx_n] = dp[idx_m - 1][idx_n - 1] + triangle[idx_m][idx_n]
                else:
                    dp[idx_m][idx_n] = min(dp[idx_m - 1][idx_n], dp[idx_m - 1][idx_n - 1]) + triangle[idx_m][idx_n]

        return int(min(dp[-1]))

test = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]


solu = Solution()
print(solu.minimumTotal(test))
