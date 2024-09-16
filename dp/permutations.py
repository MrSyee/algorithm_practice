"""
46. Permutations (Medium)
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """O(N!) / O(N), Backtracking."""
        sol, N = [], len(nums)

        def backtracking(remains, curr):
            if len(curr) == N:
                sol.append(curr)
                return
            for i in range(len(remains)):
                backtracking(remains[:i] + remains[i + 1 :], curr + [remains[i]])

        backtracking(nums, [])
        return sol
