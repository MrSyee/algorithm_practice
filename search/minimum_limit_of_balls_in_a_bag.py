"""
1760. Minimum Limit of Balls in a Bag (Medium)
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.

 

Example 1:

Input: nums = [9], maxOperations = 2
Output: 3
Explanation: 
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
Example 2:

Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.
Example 3:

Input: nums = [7,17], maxOperations = 2
Output: 7
 

Constraints:

1 <= nums.length <= 10^5
1 <= maxOperations, nums[i] <= 10^9
"""

# 실패. 제일 큰 값 반으로 나누는 전략
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def devide_half(num: int):
            if num % 2 != 0:
                h1 = num // 2
                h2 = h1 + 1
            else:
                h1 = num // 2
                h2 = h1
            return h1, h2
        
        # O(maxOperations)
        while maxOperations > 0:
            max_val = max(nums)
            nums.remove(max_val)
            nums.extend(devide_half(max_val))
            
            maxOperations -= 1
            print(nums)

        return max(nums)


# 가방 안의 공의 최대 개수를 1 ~ max(nums)까지 했을 때, operation이 몇번 필요한지 계산한다.
# max_operation와 같은 operation일 때 공 개수를 return 한다.
# 연산량을 줄이기 위해 이진 탐색 사용.
# T_C: O(log(max(nums)) * len(nums)) [O(MlogN)]
# S_C: O(1)
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # O(len(nums))
        def get_min_oper(nums: List[int], target: int):
            total_oper = 0
            for n in nums:
                total_oper += n // target - int(n % target == 0)
            return total_oper
        
        start, end = 1, max(nums)
        ans = end
        # O(log(max(nums)))
        while start < end:
            mid = (start + end) // 2
            if get_min_oper(nums, mid) <= maxOperations:
                end = ans = mid
            else:
                start = mid + 1
        return ans