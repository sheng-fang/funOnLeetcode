"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        assert isinstance(nums1, list)
        assert isinstance(nums2, list)

        m = len(nums1)
        n = len(nums2)

        assert m > 0 or n > 0

        # always assume nums1 is shorter than nums2, if not exchange the name
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        if m == 0:
            return (nums2[(n-1)//2] + nums2[n//2]) / 2

        if nums1[-1] <= nums2[0]:
            nums = nums1 + nums2
            return (nums[(n + m - 1) // 2] + nums[(n + m) // 2]) / 2

        if nums1[0] >= nums2[-1]:
            nums = nums2 + nums1
            return (nums[(n + m - 1) // 2] + nums[(n + m) // 2]) / 2
        k_min = 0
        k_max = m + 1

        while k_min <= k_max:
            k = (k_min + k_max) // 2
            l = (n + m + 1) // 2 - k

            if k > 0 and nums1[k - 1] > nums2[l]:
                k_max = (k_min + k_max) // 2
            elif k < m and nums2[l - 1] > nums1[k]:
                k_min = (k_min + k_max) // 2
            else:
                if k == m:
                    if l == 0:
                        max_left = nums1[k - 1]
                    else:
                        max_left = max(nums1[k - 1], nums2[l - 1])
                    min_right = nums2[l]
                elif k == 0:
                    max_left = nums2[l - 1]
                    min_right = min(nums1[k], nums2[l])
                else:
                    max_left = max(nums1[k - 1], nums2[l - 1])
                    min_right = min(nums1[k], nums2[l])
                return self.cal_median(n, m, max_left, min_right)

    @staticmethod
    def cal_median(n, m, max_left, min_right):
        if (n + m) % 2 == 0:
            return (max_left + min_right) / 2
        else:
            return max_left





nums1 = [5]
nums2 = [1,2,3,4,6]

solu = Solution()
print(solu.findMedianSortedArrays(nums1, nums2))
