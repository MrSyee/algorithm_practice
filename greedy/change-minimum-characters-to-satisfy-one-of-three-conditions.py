"""
1737. Change Minimum Characters to Satisfy One of Three Conditions (Medium)
https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions

You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

- Every letter in a is strictly less than every letter in b in the alphabet.
- Every letter in b is strictly less than every letter in a in the alphabet.
- Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.

 
Example 1:

Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).

Example 2:

Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".
 

Constraints:

1 <= a.length, b.length <= 105
a and b consist only of lowercase letters.
"""

from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        cnt_a, cnt_b = Counter(a), Counter(b)
        len_a, len_b = len(a), len(b)

        # dict는 +가 안되지만 Counter는 가능하다
        sol = len_a + len_b - max((cnt_a + cnt_b).values())  # cond3

        less_a, less_b = 0, 0
        for i in range(25):  # a ~ y 까지. z보다 더 커질수 없기 때문에.
            # 현재 char보다 작은 char의 개수를 체크하기 위함.
            less_a += cnt_a[chr(i + 97)]
            less_b += cnt_b[chr(i + 97)]

            # if a for cond 1(A<B), A에서 a보다 큰 char를 a로 다 바꿔야함 (len_a - less_a).
            # B에서 a보다 작은 char를 b로 다 바꿔야함 (+ less_b)
            sol = min(sol, len_a - less_a + less_b)  # cond 1
            sol = min(sol, len_b - less_b + less_a)  # cond 2

        return sol
