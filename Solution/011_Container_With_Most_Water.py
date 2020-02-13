"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution:
    def maxArea_bf(self, height: list):
        """
        brute force implementation.
        O(n*n)
        O(1)
        Args:
            height:

        Returns:

        """
        l = len(height)
        if l == 0:
            return 0

        max_area = 0
        for i in range(l):
            for j in range(i):
                tmp_area = (i - j) * min(height[i], height[j])
                if tmp_area > max_area:
                    max_area = tmp_area

        return max_area

    def maxArea(self, height: list):
        head = 0
        tail = len(height) - 1

        max_area = 0
        while tail > head:
            tmp_area = (tail - head) * min(height[tail], height[head])
            if tmp_area > max_area:
                max_area = tmp_area
            if height[tail] > height[head]:
                head += 1
            else:
                tail -= 1

        return max_area


