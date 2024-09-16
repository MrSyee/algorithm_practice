"""
42. Trapping Rain Water (Hard)
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        """Fail. O(N) / O(N)"""
        sol = 0
        for i in range(1, len(height) - 1):
            if height[i] < height[i - 1]:
                memory, n, l, r = [], i, i - 1, i + 1
                memory.append(n)
                threshold = height[r]
                while height[l] > threshold:
                    print("l", l, "r", r)
                    n, r = n + 1, r + 1
                    memory.append(n)
                    if r == len(height):
                        r = r - 1
                        memory = []
                        return sol
                    threshold = min(height[l], height[r])
                min_h = min(height[l], height[r])
                print(min_h, memory)
                sol += sum([min_h - height[m] for m in memory])
                print("sol", sol)
        return sol


class Solution:
    def trap(self, height: List[int]) -> int:
        """O(N) / O(1)"""
        sol = 0
        l, r, left, right = 0, len(height) - 1, 0, 0
        while l < r:
            if height[l] < height[r]:
                print("left", l, left, height[l])
                sol += max(left - height[l], 0)
                left = max(left, height[l])
                l += 1
            else:
                print("right", r, right, height[r])
                sol += max(right - height[r], 0)
                right = max(right, height[r])
                r -= 1
            print(sol)
        return sol
