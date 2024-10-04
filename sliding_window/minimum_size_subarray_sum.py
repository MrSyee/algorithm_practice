"""
209. Minimum Size Subarray Sum (Medium)
https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

# T_C: O(N * M)
# S_C: O(1)
# 짧은 길이부터 모든 길이의 윈도우를 탐색하다보니, 사이즈가 길면 타임아웃
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        res = float(inf)
        for i in range(length):
            left = 0
            right = left + i
            while right < length:
                subarray = [nums[left]] if left == right else nums[left:right+1]
                # print(subarray)
                if target <= sum(subarray):
                    res = min(res, i + 1)
                    break
                left += 1
                right = left + i
                # print("left, right", left, right)
                # print(res)
        return res if res != float(inf) else 0


# T_C: O(N)
# S_C: O(1)
# 윈도우의 길이를 먼저 늘려 조건을 만족하는 윈도우를 먼저 찾고 최소 사이즈를 찾는다.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        total, left, res = 0, 0, len(nums)
        for right, val in enumerate(nums):
            total += val
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res
