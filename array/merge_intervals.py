"""
56. Merge Intervals (Medium)
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Fail"""
        sol = []
        if not intervals:
            return sol
        elif len(intervals) == 1:
            return intervals
        
        first_val, last_val = intervals[0]
        for i in range(1, len(intervals)):
            next_ = intervals[i]
            if first_val > next_[0]:
                first_val = next_[0]
            
            if last_val > next_[1]:
                last_val = next_[1]
            
            if last_val < next_[0]:
                sol.append([first_val, last_val])
                first_val, last_val = next_
                if i == len(intervals) - 1:
                    sol.append(next_)
            else:
                last_val = next_[1]
                if i == len(intervals) - 1:
                    sol.append([first_val, last_val])
        
        return sol


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """O(Nlog(N))/O(N)"""
        sol = []
        if not intervals:
            return sol
        elif len(intervals) == 1:
            return intervals
        
        # sorting by first value of sub list
        intervals.sort(key=lambda x: x[0])
        first_val, last_val = intervals[0]
        for i in range(1, len(intervals)): 
            next_ = intervals[i]
            if last_val < next_[0]:
                # no merge
                sol.append([first_val, last_val])
                first_val, last_val = next_
            elif last_val < next_[1]:
                # merge
                last_val = next_[1]
            
            # last idx
            if i == len(intervals) - 1:
                sol.append([first_val, last_val])
        
        return sol


# Good Solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """O(NlogN)/O(N)"""
        sol = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if sol and sol[-1][0] <= interval[0] <= sol[-1][1]:
                sol[-1][1] = max(sol[-1][1], interval[1])
            else:
                sol.append(interval)
        return sol
