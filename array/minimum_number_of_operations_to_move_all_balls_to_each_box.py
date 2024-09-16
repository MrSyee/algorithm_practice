"""
1769. Minimum Number of Operations to Move All Balls to Each Box (Medium)
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

 

Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
Example 2:

Input: boxes = "001011"
Output: [11,8,5,4,3,4]
 

Constraints:

n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.

"""


# T_C: O(N^2)
# S_C: O(1)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for target_idx in range(len(boxes)):
            num_move = 0
            for move_idx in range(len(boxes)):
                if move_idx != target_idx and boxes[move_idx] == "1":
                    num_move += abs(target_idx - move_idx)
            ans.append(num_move)
        return ans


# T_C: O(N)
# S_C: O(1)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        num_ball, curr_cost = 0, 0
        num_ball_rev, curr_cost_rev = 0, 0
        ans = [0 for _ in range(len(boxes))]

        for idx, idx_rev in zip(range(len(boxes)), range(len(boxes) - 1, -1, -1)):
            curr_cost += num_ball
            curr_cost_rev += num_ball_rev

            ans[idx] += curr_cost
            ans[idx_rev] += curr_cost_rev

            if boxes[idx] == "1":
                num_ball += 1
            if boxes[idx_rev] == "1":
                num_ball_rev += 1

        return ans
