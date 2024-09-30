"""
12. Integer to Roman (Medium)
https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.
"""

# 48 ms, 50.73 %
class Solution:
    def intToRoman(self, num: int) -> str:
        subtractive_form = {
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }

        result = ""
        while num > 0:
            if int(str(num)[0]) == 4 or int(str(num)[0]) == 9:
                length = len(str(num))
                n = int(str(num)[0]) * (10 ** (length - 1))
                result += subtractive_form[n]
                num -= n
                continue

            if num >= 1000:
                result += "M"
                num -= 1000
            elif num >= 500:
                result += "D"
                num -= 500
            elif num >= 100:
                result += "C"
                num -= 100
            elif num >= 50:
                result += "L"
                num -= 50
            elif num >= 10:
                result += "X"
                num -= 10
            elif num >= 5:
                result += "V"
                num -= 5
            else:
                result += "I"
                num -= 1
        return result


# 조건문 줄이기
# 45 ms, 66.37 %
class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }

        result = ""
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while num >= n:
                result += num_map[n]
                num -= n

        return result