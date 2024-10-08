"""
202. Happy Number (Easy)
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """O(N^2)/O(N)"""
        for _ in range(100):
            nums = [int(s) for s in str(n)]
            if sum(nums) == 1:
                return True
            n = sum([nn**2 for nn in nums])
        return False


class Solution:
    def isHappy(self, n: int) -> bool:
        prev = []
        while n not in prev:
            prev.append(n)
            nums = [int(s) for s in str(n)]
            if sum(nums) == 1:
                return True
            n = sum([nn**2 for nn in nums])
        return False
