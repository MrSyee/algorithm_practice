"""
228. Summary Ranges (Easy)
https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""
# T_C: O(N)
# S_C: O(N)
# 24ms, 97.72
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
            
        ans = []
        ans_list = [nums[0]]
        cur = nums[0]

        for n in nums[1:]:
            print(n, ans_list)
            if n - cur == 1:
                ans_list.append(n)
            else:
                ans_str = str(ans_list[0]) if len(ans_list) == 1 else f"{ans_list[0]}->{ans_list[-1]}"
                ans.append(ans_str)
                ans_list = [n]
            cur = n
        ans_str = str(ans_list[0]) if len(ans_list) == 1 else f"{ans_list[0]}->{ans_list[-1]}"
        ans.append(ans_str)
        return ans
