"""
1753. Maximum Score From Removing Stones (Medium)
https://leetcode.com/problems/maximum-score-from-removing-stones/

You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.

 

Example 1:

Input: a = 2, b = 4, c = 6
Output: 6
Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
- Take from 1st and 3rd piles, state is now (1, 4, 5)
- Take from 1st and 3rd piles, state is now (0, 4, 4)
- Take from 2nd and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 6 points.
Example 2:

Input: a = 4, b = 4, c = 6
Output: 7
Explanation: The starting state is (4, 4, 6). One optimal set of moves is:
- Take from 1st and 2nd piles, state is now (3, 3, 6)
- Take from 1st and 3rd piles, state is now (2, 3, 5)
- Take from 1st and 3rd piles, state is now (1, 3, 4)
- Take from 1st and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 7 points.
Example 3:

Input: a = 1, b = 8, c = 8
Output: 8
Explanation: One optimal set of moves is to take from the 2nd and 3rd piles for 8 turns until they are empty.
After that, there are fewer than two non-empty piles, so the game ends.
 

Constraints:

1 <= a, b, c <= 10^5
"""


# T_C: O(max(a, b, c) * 3 * 3)
# S_C: O(3)
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # O(3)
        def min_except_zero(list_: list):
            minval = min(list_)
            if minval == 0:
                tmp_list = list_.copy()
                tmp_list.remove(0)
                minval = min(tmp_list)
            return minval

        count = 0
        score = [a, b, c]

        # O(max(score)), 2개 이상의 값이 0이 되면 종료
        while not (
            (score[0] + score[1]) == 0
            or (score[1] + score[2]) == 0
            or (score[0] + score[2]) == 0
        ):
            # 가장 큰 값과 작은 값을 하나씩 줄인다.
            minidx = score.index(min_except_zero(score))
            maxidx = score.index(max(score))

            if minidx == maxidx:
                minidx = (minidx + 1) % len(score)
                while score[minidx] == 0:
                    minidx = (minidx + 1) % len(score)

            score[minidx] = score[minidx] - 1
            score[maxidx] = score[maxidx] - 1

            count += 1

        return count
