"""
54. Spiral Matrix (Medium)
https://leetcode.com/problems/spiral-matrix/description/?source=submission-ac

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

# T_C: O(m * n)
# S_C: O(1)
# 29ms, 89.94%
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left_bound, right_bound = 0, n - 1
        top_bound, bot_bound = 1, m - 1
        row_bound, col_bound = bot_bound, right_bound
        r, c = 0, 0
        dr, dc = 0, 1

        ans = []
        for _ in range(m * n):
            ans.append(matrix[r][c])

            if (r == row_bound and dr != 0) or (c == col_bound and dc != 0):
                if r == row_bound and dr > 0:
                    row_bound = top_bound
                    bot_bound -= 1
                if r == row_bound and dr < 0:
                    row_bound = bot_bound
                    top_bound += 1
                if c == col_bound and dc > 0:
                    col_bound = left_bound
                    right_bound -= 1
                if c == col_bound and dc < 0:
                    col_bound = right_bound
                    left_bound += 1

                dr, dc = dc, -dr

            r += dr
            c += dc
        return ans


# 같은 로직인데, 들렀던 곳을 "."으로 채워 코드가 간소화되는 로직
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        dr, dc = 0, 1

        ans = []
        for _ in range(m * n):
            ans.append(matrix[r][c])
            matrix[r][c] = "."

            if not 0 <= r + dr < m or not 0 <= c + dc < n or matrix[r + dr][c + dc] == ".":
                dr, dc = dc, -dr

            r += dr
            c += dc

        return ans
