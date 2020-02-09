class Solution:
    def reverse(self, x: int) -> int:
        ele_list = []
        if x == 0:
            return 0
        elif x < 0:
            tmp_x = -x
            flag = -1
        else:
            tmp_x = x
            flag = 1

        while tmp_x > 0:
            ele_list.append(tmp_x % 10)
            tmp_x = tmp_x // 10

        reverse_val = 0
        for idx, ele in enumerate(ele_list):
            reverse_val += ele
            reverse_val *= 10

        return reverse_val * flag
