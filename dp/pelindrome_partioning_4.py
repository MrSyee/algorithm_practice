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

# T_C: O(N^2)
# S_C: O(N^2)
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        # O(N). len(s)^2 만큼의 배열 생성
        is_palindrome = []
        for _ in range(len(s)):
            is_palindrome.append([False for _ in range(len(s))])
        
        # O(N). len 1, 2 pelindrome 여부 체크
        for i in range(len(s)):
            is_palindrome[i][i] = True
            if i < len(s)- 1 and s[i] == s[i+1]:
                is_palindrome[i][i+1] = True
        
        # O(N^2). len >= 3 pelindrome 여부 체크
        for i in range(2, len(s)):
            for j in range(len(s) - i):
                if s[j] == s[j+i] and is_palindrome[j+1][j+i-1]:
                    is_palindrome[j][j+i] = True
        
        # O(N^2). 문자열 분리 위치 찾기
        for i in range(0, len(s)-2):
            for j in range(1, len(s) - 1):
                if is_palindrome[0][i] and is_palindrome[i+1][j] and is_palindrome[j+1][len(s)-1]:
                    return True
        return False
