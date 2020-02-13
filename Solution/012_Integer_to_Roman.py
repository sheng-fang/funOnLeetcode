"""
https://leetcode.com/problems/integer-to-roman/description/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is
simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        tmp_num = num
        digit_list = []

        while tmp_num > 0:
            curr_digit = tmp_num % 10
            digit_list.append(curr_digit)
            tmp_num = tmp_num // 10

        roman_str=''
        for i in range(len(digit_list) - 1, -1, -1):
            if i == 3:
                roman_str += 'M' * digit_list[i]

            if i == 2:
                if digit_list[i] < 4:
                    roman_str += "C" * digit_list[i]
                elif digit_list[i] == 4:
                    roman_str += "CD"
                elif digit_list[i] == 5:
                    roman_str += "D"
                elif digit_list[i] < 9:
                    roman_str += ("D" + "C" * (digit_list[i] - 5))
                else:
                    roman_str += "CM"

            if i == 1:
                if digit_list[i] < 4:
                    roman_str += "X" * digit_list[i]
                elif digit_list[i] == 4:
                    roman_str += "XL"
                elif digit_list[i] == 5:
                    roman_str += "L"
                elif digit_list[i] < 9:
                    roman_str += ("L" + "X" * (digit_list[i] - 5))
                else:
                    roman_str += "XC"

            if i == 0:
                if digit_list[i] < 4:
                    roman_str += "I" * digit_list[i]
                elif digit_list[i] == 4:
                    roman_str += "IV"
                elif digit_list[i] == 5:
                    roman_str += "V"
                elif digit_list[i] < 9:
                    roman_str += ("V" + "I" * (digit_list[i] - 5))
                else:
                    roman_str += "IX"

        return roman_str


test = 58
solu = Solution()
print(solu.intToRoman(test))
