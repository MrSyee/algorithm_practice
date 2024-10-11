"""
200. Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

# T_C: O(m * n)
# S_C: O(m * n)
# 239 ms. 66.47
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited_island = [[False] * n for _ in range(m)]
        ans = 0

        for row in range(m):
            for col in range(n):
                if visited_island[row][col] or grid[row][col] == "0":
                    visited_island[row][col] = True
                    continue

                stack = [(row, col)]
                while stack:
                    curr_row, curr_col = stack.pop(0)
                    if grid[curr_row][curr_col] == "0":
                        continue

                    next_row = curr_row + 1
                    next_col = curr_col + 1
                    prev_row = curr_row - 1
                    prev_col = curr_col - 1

                    if (prev_row, curr_col) not in stack and prev_row >= 0 and not visited_island[prev_row][curr_col]:
                        stack.append((prev_row, curr_col))
                    if (curr_row, prev_col) not in stack and prev_col >= 0 and not visited_island[curr_row][prev_col]:
                        stack.append((curr_row, prev_col))
                    if (next_row, curr_col) not in stack and next_row < m and not visited_island[next_row][curr_col]:
                        stack.append((next_row, curr_col))
                    if (curr_row, next_col) not in stack and next_col < n and not visited_island[curr_row][next_col]:
                        stack.append((curr_row, next_col))

                    visited_island[curr_row][curr_col] = True
                ans += 1
        return ans
