"""
1786. Number of Restricted Paths From First to Last Node (Medium)
https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

 

Example 1:


Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5
Example 2:


Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.
 

Constraints:

1 <= n <= 2 * 10^4
n - 1 <= edges.length <= 4 * 10^4
edges[i].length == 3
1 <= ui, vi <= n
ui != vi
1 <= weighti <= 10^5
There is at most one edge between any two nodes.
There is at least one path between any two nodes.
"""
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # dict로 graph 구조를 만든다.
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u].update({v: w})
            graph[v].update({u: w})
        
        # 각 노드들의 n 노드까지의 최소 거리를 구한다.
        distances = {node: float("inf") for node in graph}
        distances[n] = 0
        queue = []
        heapq.heappush(queue, [distances[n], n])
        
        while queue:
            curr_distance, curr_node = heapq.heappop(queue)
            
            if distances[curr_node] < curr_distance:
                continue
            
            for next_node, next_distance in graph[curr_node].items():
                distance = curr_distance + next_distance
                if distance < distances[next_node]:
                    distances[next_node] = distance
                    heapq.heappush(queue, [distance, next_node])
        
        # DP: Memoization
        def dfs(node):
            if node == 1:
                return 1
            if node not in memo:
                memo[node] = sum(dfs(v) for v in graph[node].keys() if distances[v] > distances[node])
            return memo[node] % (10 ** 9 + 7)
        memo = collections.defaultdict(int)
        return dfs(n)