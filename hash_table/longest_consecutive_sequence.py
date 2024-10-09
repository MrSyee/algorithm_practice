"""
128. Longest Consecutive Sequence (Medium)
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
# T_C: O(N) 
# S_C: O(N)
# 345ms, 73.20%
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
    
        nums = sorted(list(set(nums)))
        
        ans = 0
        tmp_list = [nums[0]]
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                tmp_list.append(nums[i+1])
            else:
                ans = max(ans, len(tmp_list))
                tmp_list = [nums[i+1]]

        return max(ans, len(tmp_list))
