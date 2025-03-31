"""
15. 3Sum (Medium)
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
# 풀이

1. Two pointers 활용
2. 정렬
3. 합이 0이 되어야하므로 반복하면서 합이 0보다 작은지, 큰지에 따라 pointer를 움직임
4. 중복 제거
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """O(N^3)/O(1)"""
        sol = []
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    tmp = sorted([nums[i], nums[j], nums[k]])
                    if sum(tmp) == 0 and tmp not in sol:
                        sol.append(tmp)
        return sol


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """O(N^2)/O(1)"""
        sol = []
        nums.sort()
        n = len(nums)

        if n < 3:
            return []

        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l_idx = i + 1
            r_idx = n - 1

            while l_idx < r_idx:
                s = nums[i] + nums[l_idx] + nums[r_idx]
                if s < 0:
                    l_idx += 1
                elif s > 0:
                    r_idx -= 1
                else:
                    sol.append([nums[i], nums[l_idx], nums[r_idx]])
                    while l_idx < n - 1 and nums[l_idx] == nums[l_idx + 1]:
                        l_idx += 1
                    while r_idx > i + 1 and nums[r_idx - 1] == nums[r_idx]:
                        r_idx -= 1

                    l_idx += 1
                    r_idx -= 1

        return sol
