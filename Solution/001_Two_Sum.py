class Solution:
    def twoSum(self, nums: list, target: int):
        assert isinstance(target, int)
        assert isinstance(nums, list)

        pair_rec = dict()
        for idx, elem in enumerate(nums):
            if elem in pair_rec:
                return idx, pair_rec[elem]
            else:
                pair_rec[target - elem] = idx

        return None
