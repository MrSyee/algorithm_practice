"""
3. Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Time Limit Exceeded. O(N^2)/O(N)"""
        if not s:
            return 0
        sol_list = [1]
        for idx in range(len(s)):
            l_idx = idx
            tmp_str = s[l_idx]
            for r_idx in range(l_idx+1, len(s)):
                if s[r_idx - 1] is not s[r_idx] and s[r_idx] not in tmp_str:
                    tmp_str += s[r_idx]
                else:
                    sol_list.append(len(tmp_str))
                    l_idx = r_idx
                    tmp_str = s[l_idx]
            sol_list.append(len(tmp_str))
        return max(sol_list)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """O(N)/O(1)"""
        d = dict()
        left = -1
        right = 0
        sol = 0
        while right < len(s):
            if s[right] in d and left < d[s[right]]:
                left = d[s[right]]
                d[s[right]] = right
            else:
                d[s[right]] = right
                sol = max(sol, right - left)
            right += 1
        return sol