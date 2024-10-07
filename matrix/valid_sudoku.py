"""
36. Valid Sudoku (Medium)
https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

# T_C: O(1)
# S_C: O(1)
# 90ms, 68.51%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # print("Row")
        for row in board:
            tmp = set()
            for e in row:
                if e in tmp and e != ".":
                    return False
                tmp.add(e)
                # print(tmp)
        
        # print("Col")
        for col_idx in range(9):
            tmp = set()
            for row_idx in range(9):
                if board[row_idx][col_idx] in tmp and board[row_idx][col_idx] != ".":
                    return False
                tmp.add(board[row_idx][col_idx])
                # print(tmp)
        
        # print("Sub-box")
        row = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        col = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        for n in range(9):
            tmp = set()
            col = [c + 3 for c in col]
            if n % 3 == 0:
                row = [n] * 3 + [n + 1] * 3 + [n + 2] * 3
                col = [0, 1, 2] * 3
            
            for i in range(9):
                if board[row[i]][col[i]] in tmp and board[row[i]][col[i]] != ".":
                    return False
                tmp.add(board[row[i]][col[i]])
                # print(tmp)
        return True


# 더 간소화된 버전. 한번의 반복문에서 모든 조건 체크.
# defaultdict + set을 각각의 조건에 맞는 원소들을 저장.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True