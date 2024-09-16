"""
1743. Restore the Array From Adjacent Pairs (Medium)
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

 

Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]
 

Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 10^5
-10^5 <= nums[i], ui, vi <= 10^5
There exists some nums that has adjacentPairs as its pairs.
"""


# T_C: O(N)
# S_C: O(N)
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def add_to_dict(a_dict, key, val):
            if key in a_dict:
                a_dict[key].append(val)
            else:
                a_dict[key] = [val]
            return a_dict

        adjacent_dict = dict()
        for ad in adjacentPairs:  # O(n)
            adjacent_dict = add_to_dict(adjacent_dict, ad[0], ad[1])
            adjacent_dict = add_to_dict(adjacent_dict, ad[1], ad[0])

        # 연결된 숫자가 하나 밖에 없는 수를 찾는다.
        adj_only_one = []
        for k, v in adjacent_dict.items():
            if len(v) == 1:
                adj_only_one.append(k)

        # 0으로 채워진 리스트를 만든다.
        ans = []
        for _ in range(len(adjacentPairs) + 1):
            ans.append(0)

        # 연결된 숫자가 하나인 수를 양 끝에 채운다.
        ans[0] = adj_only_one[0]
        ans[-1] = adj_only_one[1]

        # 맨 앞 수부터 연결된 숫자를 하나씩 채워간다.
        # 채워진 숫자는 연결된 숫자에서 지운다.
        for i in range(len(ans) - 1):
            adj = adjacent_dict[ans[i]][0]
            adjacent_dict[adj].remove(ans[i])
            ans[i + 1] = adj

        return ans
