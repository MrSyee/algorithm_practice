"""
7. Reverse Integer (Medium)
https://leetcode.com/problems/reverse-integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        rev = int(str(abs(x))[-1::-1])
        if negative:
            rev *= -1
        return rev if -(2**31) <= rev <= 2**31 - 1 else 0
