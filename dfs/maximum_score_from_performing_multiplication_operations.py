"""
1770. Maximum Score from Performing Multiplication Operations (Medium)
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

 

Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 10^3
m <= n <= 10^5
-1000 <= nums[i], multipliers[i] <= 1000
"""

# DFS(Backtracking), Time Limit Exceeded..
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        if len(multipliers) == 0:
            return 0
        
        else:
            sum_f = multipliers[0] * nums[0] + self.maximumScore(nums[1:], multipliers[1:])
            sum_b = multipliers[0] * nums[-1] + self.maximumScore(nums[:-1], multipliers[1:])
            return max(sum_f, sum_b)


# use lru_cache limit
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def dfs(left, right, mul_idx):
            if mul_idx == len(multipliers):
                return 0

            else:
                sum_f = multipliers[mul_idx] * nums[left] + dfs(left + 1, right, mul_idx + 1)
                sum_b = multipliers[mul_idx] * nums[right] + dfs(left, right - 1, mul_idx + 1)
                return max(sum_f, sum_b)

        return dfs(0, len(nums) - 1, 0)