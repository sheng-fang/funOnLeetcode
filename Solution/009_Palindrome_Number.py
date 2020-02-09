class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0 or x < 10:
            return True

        dig_list = []

        tmp_x = x

        while tmp_x > 0:
            dig_list.append(tmp_x%10)
            tmp_x //=10

        dig_len = len(dig_list)

        for idx, value in enumerate(dig_list):
            if idx <= dig_len - idx - 1:
                if dig_list[idx] == dig_list[dig_len - idx - 1]:
                    continue
                else:
                    return False
            else:
                return True


t = Solution()
print(t.isPalindrome(22222))
