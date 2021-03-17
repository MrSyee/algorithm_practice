"""
1775. Equal Sum Arrays With Minimum Number of Operations (Medium)
https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

 

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
"""
# Fail
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        s1, s2 = sum(nums1), sum(nums2)
        l1, l2 = len(nums1), len(nums2)
        diff = abs(s1 - s2)
        
        sol = float("inf")
        if s1 == s2:
            return 0
        
        elif s1 < s2:
            # num2 줄이기
            right = len(nums2) - 1
            for i in range(len(nums2)):
                diff = diff - (6 - nums2[right - i])
                if diff <= 0:
                    sol = min(sol, (len(nums2) - 1) - (right - i))
            
            # num1 늘리기
            left = 0
            for i in range(len(nums1)):
                diff = diff - (nums1[left + i] - 1)
                if diff <= 0:
                    sol = min(sol, left + i)
        
        else:
            # num1 줄이기
            right = len(nums1) - 1
            for i in range(len(nums1)):
                diff = diff - (6 - nums1[right - i])
                if diff <= 0:
                    sol = min(sol, (len(nums1) - 1) - (right - i))
            
            # num1 늘리기
            left = 0
            for i in range(len(nums2)):
                diff = diff - (nums2[left + i] - 1)
                if diff <= 0:
                    sol = min(sol, left + i)
        return sol
            
                
                