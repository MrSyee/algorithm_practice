"""
1759. Count Number of Homogenous Substrings (Medium)
https://leetcode.com/problems/count-number-of-homogenous-substrings/

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
Example 3:

Input: s = "zzzzz"
Output: 15
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase letters.
"""

# T_C: O(len(s)) <  < O(len(s)^2)
# S_C: O(1)
class Solution:
    def countHomogenous(self, s: str) -> int:
        if len(s) == 1:
            return 1
        sol, left, right = 0, 0, 0
        while left < len(s) - 1 and right < len(s) - 1:
            curr = s[left]
            for plus_idx in range(len(s) - left):
                right = left + plus_idx
                if curr != s[right]:  # curr char와 다르면
                    left = right
                    sol += (plus_idx * (plus_idx + 1)) // 2  # ex. len = 3: 3+2+1    
                    break
        last = right - left + 1
        sol += (last * (last + 1)) // 2
        return int(sol % (1e9+7))


# Discuss solution
# T_C: O(N)
# S_C: O(N)
class Solution:
    def countHomogenous(self, s: str) -> int:
        arr = [1]
        
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                arr.append(arr[i-1]+1)
                
            else:
                arr.append(1)
                
        return int(sum(arr)%(1e9+7))