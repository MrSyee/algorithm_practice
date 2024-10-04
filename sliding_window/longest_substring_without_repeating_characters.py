"""
3. Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# T_C: O(N * M)
# S_C: O(1)
# 305ms, 9.06%
# 중복된 것이 나왔을 경우 left와 right를 모두 리셋하니 시간이 더 걸린다.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
    
        length = len(s)
        left, right = 0, 0
        ans = 0

        substring = ""

        while left <= right and right < length:
            if s[right] not in substring:
                substring += s[right]
                right += 1
            else:
                ans = max(ans, right - left)
                left += 1
                right = left
                substring = ""
        return max(ans, right - left)


# T_C: O(N)
# S_C: O(1)
# 38ms, 99.32%
# left 위치가 중복된 알파벳의 다음으로 이동하도록 해주면 시간을 아낄 수 있다.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
    
        length = len(s)
        left, right = 0, 0
        ans = 0

        char_dict = {}

        for right in range(length):
            if s[right] not in char_dict or char_dict[s[right]] < left:
                char_dict[s[right]] = right
                ans = max(ans, right - left + 1)
            else:
                left = char_dict[s[right]] + 1
                char_dict[s[right]] = right
        return ans
        