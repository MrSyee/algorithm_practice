"""
31. Next Permutation (Medium)
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        O(N) / O(1)
        Do not return anything, modify nums in-place instead.
        """
        l = -1
        # Find the last index among the indexes with a higher value than itself
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                l = i - 1
        if l == -1:
            nums.reverse()
            return
        
        # Find last index among the indexes with a higher value than value of l index
        r = 0
        for j in range(l + 1, len(nums)):
            if nums[j] > nums[l]:
                r = j
        
        # Swap values for each index
        nums[l], nums[r] = nums[r], nums[l]
        
        # Sort next parts of l index
        tmp_nums = sorted(nums[l + 1:])
        nums[l + 1:] = tmp_nums
        
        return


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        O(N) / O(1)
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = len(nums) - 1
                while j > i - 1:
                    if nums[j] > nums[i - 1]:
                        break
                    j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                tmp_nums = sorted(nums[i:])
                nums[i:] = tmp_nums
                return
        nums.reverse()        
        return
