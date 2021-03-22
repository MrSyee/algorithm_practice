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
# 1452 ms
# T_C: O(n1 + n2)
# S_C: O(1)
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if sum(nums1) == sum(nums2):
            return 0

        if sum(nums1) > sum(nums2):
            nums1, nums2 = nums2, nums1
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)[::-1]
        diff = sum(nums2) - sum(nums1)
        max_len = len(nums1) + len(nums2)
        
        # 갭이 큰 숫자부터 줄이거나 늘린다.
        i1 = i2 = 0
        while i1 + i2 < max_len:
            gap1 = 6 - nums1[i1] if len(nums1) > i1 else -1
            gap2 = nums2[i2] - 1 if len(nums2) > i2 else -1
            
            if gap1 >= gap2:
                diff = diff - gap1
                i1 += 1
            else:
                diff = diff - gap2
                i2 += 1
            if diff <= 0:
                return i1 + i2
        return -1


# 조금 더 빠름 (1228 ms)
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sums = [sum(nums1), sum(nums2)]
        nums = [nums1, nums2]
        
        if sums[1] < sums[0]:
            sums = [sums[1], sums[0]]
            nums = [nums2, nums1]
            
        difference = sums[1] - sums[0]
        output = 0
        difference_reduction_to_frequency = [0] * 6
        for number in nums[0]:
            difference_reduction_to_frequency[6 - number] += 1
            
        for number in nums[1]:
            difference_reduction_to_frequency[number - 1] += 1
            
        for difference_reduction in range(5, 0, -1):
            frequency = difference_reduction_to_frequency[difference_reduction]
            total_difference_reduction = difference_reduction * frequency
            
            if total_difference_reduction >= difference:
                return output + ceil(difference / difference_reduction)
            else:
                output += frequency
                difference -= total_difference_reduction
                
        return -1
