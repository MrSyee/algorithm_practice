"""
1745. Palindrome Partitioning IV (Hard)
https://leetcode.com/problems/palindrome-partitioning-iv/

Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

 

Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.
 

Constraints:

3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.
"""

from collections import defaultdict

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def is_pelindrom(string):
            if len(string) % 2 == 0
                mid = len(string) // 2 - 1
                if string[0:mid] == string[::-mid]:
                    return True
                else:
                    return False
            else:
                mid = len(string) // 2
                if string[0:mid-1] == string[::-(mid-1)]:
                    return True
                else:
                    return False
        
        pelindromes = defaultdict(list)
        i = 0
        for j in range(len(s)):
            if i == j:
                pelindrome[i].append(i)
                continue
            
            if is_pelindrom(s[i:j]):
                pelindromes[i].append(j)
        
        for ii in pelindromes[i]:
            for j in range(len(s) - ii + 1):
                if ii == j:
                    pelindrome[ii].append(ii)
                    continue

                if is_pelindrom(s[ii:j]):
                    pelindromes[ii].append(j) 
            
        