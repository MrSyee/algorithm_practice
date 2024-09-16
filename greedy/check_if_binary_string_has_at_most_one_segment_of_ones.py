"""
1784. Check if Binary String Has at Most One Segment of Ones (Easy)
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # 없어도 되는데 있으면 좀 더 빠름
        if len(s) == 1 and s[0] == "1":
            return True

        is_zero = False
        for i in range(len(s)):
            if s[i] == "0" and not is_zero:
                is_zero = True
            if is_zero:
                if s[i] == "1":
                    return False
        return True
