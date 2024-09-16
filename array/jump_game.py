"""
55. Jump Game (Medium)
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

from typing import List


# T_C:
# S_C:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DFS 방식으로 풀어보려함.
        # Fail: Time Limit Exceeded
        answer =  False

        last_index = len(nums) - 1
        first_index = 0
        index_cand = [first_index]

        while index_cand:
            index = index_cand.pop(0)
            value = nums[index]

            if index == last_index:
                answer = True
                break

            if value == 0:
                continue

            next_cand = [index + v for v in range(1, value + 1) if index + v <= last_index]
            index_cand = next_cand + index_cand

        return answer


# T_C: O(N)
# S_C: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i

        return True if last_index == 0 else False