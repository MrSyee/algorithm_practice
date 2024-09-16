"""
1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number (Medium)
https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

You are given a string num, representing a large integer, and an integer k.

We call some integer wonderful if it is a permutation of the digits in num and is greater in value than num. There can be many wonderful integers. However, we only care about the smallest-valued ones.

For example, when num = "5489355142":
The 1st smallest wonderful integer is "5489355214".
The 2nd smallest wonderful integer is "5489355241".
The 3rd smallest wonderful integer is "5489355412".
The 4th smallest wonderful integer is "5489355421".
Return the minimum number of adjacent digit swaps that needs to be applied to num to reach the kth smallest wonderful integer.

The tests are generated in such a way that kth smallest wonderful integer exists.

 

Example 1:

Input: num = "5489355142", k = 4
Output: 2
Explanation: The 4th smallest wonderful number is "5489355421". To get this number:
- Swap index 7 with index 8: "5489355142" -> "5489355412"
- Swap index 8 with index 9: "5489355412" -> "5489355421"
Example 2:

Input: num = "11112", k = 4
Output: 4
Explanation: The 4th smallest wonderful number is "21111". To get this number:
- Swap index 3 with index 4: "11112" -> "11121"
- Swap index 2 with index 3: "11121" -> "11211"
- Swap index 1 with index 2: "11211" -> "12111"
- Swap index 0 with index 1: "12111" -> "21111"
Example 3:

Input: num = "00123", k = 1
Output: 1
Explanation: The 1st smallest wonderful number is "00132". To get this number:
- Swap index 3 with index 4: "00123" -> "00132"
 

Constraints:

2 <= num.length <= 1000
1 <= k <= 1000
num only consists of digits.

"""


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def get_next_permutation(num: List[int]) -> List[int]:
            # T_C: O(N)
            # S_C: O(1)
            # num[i] < num[i+1]을 만족하는 가장 큰 i를 찾는다.
            swap_i = -1
            for i in range(len(num) - 1):
                if num[i] < num[i + 1]:
                    swap_i = i

            # num[swap_i] < num[j]를 만족하는 가장 큰 j를 찾는다.
            swap_j = -1
            for j in range(len(num) - 1, swap_i, -1):
                if num[swap_i] < num[j]:
                    swap_j = j
                    break
            # num[swap_i]와 num[swap_j]를 swap한다.
            num[swap_i], num[swap_j] = num[swap_j], num[swap_i]

            # num[swap_i + 1:]을 reverse 정렬한다.
            num[swap_i + 1 :] = reversed(num[swap_i + 1 :])

            return num

        def calculate_adjacent_swaps(origin: List[int], target: List[int]) -> int:
            origin_idx = target_idx = 0
            swaps = 0

            while origin_idx < len(origin):
                if origin[origin_idx] == target[target_idx]:
                    origin_idx += 1
                    target_idx += 1
                else:
                    while origin[origin_idx] != target[target_idx]:
                        target_idx += 1
                    while target[origin_idx] != target[target_idx]:
                        target[target_idx], target[target_idx - 1] = (
                            target[target_idx - 1],
                            target[target_idx],
                        )
                        target_idx -= 1
                        swaps += 1
            return swaps

        # Main
        origin = [int(n) for n in num]
        target = [int(n) for n in num]
        # k 번째 순열을 구한다.
        for _ in range(k):
            target = get_next_permutation(target)
        # swap 횟수를 구한다.
        swaps = calculate_adjacent_swaps(origin, target)

        return swaps
