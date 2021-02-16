"""
1744. Can You Eat Your Favorite Candy on Your Favorite Day? (Medium)
https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

You are given a (0-indexed) array of positive integers candiesCount where candiesCount[i] represents the number of candies of the ith type you have. You are also given a 2D array queries where queries[i] = [favoriteTypei, favoriteDayi, dailyCapi].

You play a game with the following rules:

You start eating candies on day 0.
You cannot eat any candy of type i unless you have eaten all candies of type i - 1.
You must eat at least one candy per day until you have eaten all the candies.
Construct a boolean array answer such that answer.length == queries.length and answer[i] is true if you can eat a candy of type favoriteTypei on day favoriteDayi without eating more than dailyCapi candies on any day, and false otherwise. Note that you can eat different types of candy on the same day, provided that you follow rule 2.

Return the constructed array answer.

 

Example 1:

Input: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
Output: [true,false,true]
Explanation:
1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you will eat a candy of type 0 on day 2.
2- You can eat at most 4 candies each day.
   If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and 4 candies (type 0 and type 1) on day 1.
   On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a candy of type 4 on day 2.
3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.
Example 2:

Input: candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
Output: [false,true,true,false,false]
 

Constraints:

1 <= candiesCount.length <= 10^5
1 <= candiesCount[i] <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 3
0 <= favoriteTypei < candiesCount.length
0 <= favoriteDayi <= 10^9
1 <= dailyCapi <= 10^9
"""

# 하루에 먹을수 있는 개수를 한 가지 수로 고정했을 때만 구함
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        for query in queries:  # O(queries)
            target_type, target_day, day_cap = query
            
            n_target = candiesCount[target_type]
            n_candies = sum(candiesCount[:target_type])
            
            cap = 1
            is_eat = False
            while cap <= day_cap:  # O(queries * day_cap)
                n_eating = n_candies - ((target_day + 1) * cap)
                if n_eating > 0 and n_eating <= n_target:
                    is_eat = True
                    break
                cap += 1
            ans.append(is_eat)

        return ans


# 힌트 봄. 가능한 날짜의 최대 최소를 구하여 그 사이에 들어올 경우 통과. but, timelimit..
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        for target_type, target_day, day_cap in queries:  # O(queries)
            n_target = candiesCount[target_type]
            n_smaller_candies = sum(candiesCount[:target_type])  # O(target_type)
            
            is_eat = False
            # eariest
            eariest_day = n_smaller_candies // day_cap
            # latest
            latest_day = n_smaller_candies + n_target
            
            if eariest_day <= target_day < latest_day:  # latest day 등호 안됨
                is_eat = True
            ans.append(is_eat)
        
        return ans


# Discuss 봄. 누적합을 미리 계산해 두고 사용한다. Discuss에서는 accumulate 이용.
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        accum = 0
        accum_candies = []
        for n_candies in candiesCount:  # O(candiesCount)
            accum += n_candies
            accum_candies.append(accum)

        for target_type, target_day, day_cap in queries:  # O(queries)
            is_eat = False
            # eariest
            if target_type > 0:
                eariest_day = accum_candies[target_type - 1] // day_cap
            else:
                eariest_day = 0
            # latest
            latest_day = accum_candies[target_type]
            
            if eariest_day <= target_day < latest_day:
                is_eat = True
            ans.append(is_eat)
        
        return ans