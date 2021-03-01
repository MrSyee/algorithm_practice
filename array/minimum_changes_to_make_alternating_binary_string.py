 """
1758. Minimum Changes To Make Alternating Binary String (Easy)
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 10^4
s[i] is either '0' or '1'.
"""
# T_C: O(len(s))
# S_C: O(len(s))
class Solution:
    def minOperations(self, s: str) -> int:
        target1, target2 = "", ""
        
        target1 = "".join(["0" if (i+1) % 2 != 0 else "1" for i in range(len(s))])
        target2 = "".join(["1" if (i+1) % 2 != 0 else "0" for i in range(len(s))])

        diff_from_t1 = (sum([s[i] != target1[i] for i in range(len(s))]))
        diff_from_t2 = (sum([s[i] != target2[i] for i in range(len(s))]))
        
        return min(diff_from_t1, diff_from_t2)


# T_C: O(len(s))
# S_C: O(1)
class Solution:
    def minOperations(self, s: str) -> int:
        cnt_01, cnt_10 = 0, 0
        for i in range(len(s)):
            if i % 2 == 0:
                cnt_10 += int(s[i] == "0")
            else:
                cnt_10 += int(s[i] == "1")
                
            if i % 2 == 0:
                cnt_01 += int(s[i] == "1")
            else:
                cnt_01 += int(s[i] == "0")
                
        return min(cnt_01, cnt_10)