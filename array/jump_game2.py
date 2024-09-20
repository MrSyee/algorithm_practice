"""
45. Jump Game II (Medium)
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

from typing import List


# T_C: O(len(nums)-1 * M)
# S_C: O(len(nums)-1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP 방식으로 풀어. 1541 ms Beats 23.40%
        length = len(nums)
        if length == 1:
            return 0
        r_reach = [length - 1] * (length - 1)
        # [4, 4, 4, 4]
        # [4, 4, 4, 1]
        # [2, 1, 2, 1]
        for i in range(length - 2, -1, -1):
            if length - 1 - i <= nums[i]:
                r_reach[i] = 1
            else:
                min_reach = length - 1
                count = nums[i]
                while count > 0:
                    next_idx = i + count
                    min_reach = r_reach[next_idx] + 1 if min_reach > r_reach[next_idx] + 1 else min_reach
                    count -= 1
                r_reach[i] = min_reach
        return r_reach[0]
