"""
5. Longest Palindromic Substring (Medium)
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """O(N^2) / O(N), 8680 ms"""
        if s == s[::-1]:
            return s
        sol = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if len(substring) is 1 and len(sol) < len(substring):
                    sol = substring
                elif len(substring) % 2 is 0 and len(sol) < len(substring):
                    half = len(substring) // 2
                    if substring[:half] == substring[half:][::-1]:
                        sol = substring
                elif len(substring) % 2 is not 0 and len(sol) < len(substring):
                    half = len(substring) // 2
                    if substring[:half] == substring[half+1:][::-1]:
                        sol = substring
        return sol if sol else s
