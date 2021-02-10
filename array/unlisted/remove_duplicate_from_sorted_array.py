from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)
        
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 2]))
