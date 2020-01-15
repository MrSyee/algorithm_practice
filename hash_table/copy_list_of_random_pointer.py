"""
138. Copy List with Random Pointer (Medium)
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example 4:
Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 
Constraints:
-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """Fail. O(N)/O(N)
           If the key of val2idx is duplicated, it outputs wrong answer.
        """
        node_list = []
        randval_list = []
        val2idx = {}
        i = 0
        while head:
            new_node = Node(head.val)
            node_list.append(new_node)
            if i > 0:
                prev_node.next = new_node
            prev_node = new_node
            randval = head.random.val if head.random else None
            randval_list.append(randval)
            if head.val not in val2idx:
                # if the key of val2idx is duplicated
                val2idx[head.val] = i
            head = head.next
            i += 1
        
        for i, randval in enumerate(randval_list):
            node_list[i].random = node_list[val2idx[randval]] if randval else None
        
        return node_list[0] if node_list else None


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """O(N)/O(N)"""
        old1 = old2 = head
        old2new = {None: None}
        i = 0
        while old1:
            new_node = Node(old1.val)
            old2new[old1] = new_node
            if i > 0:
                prev_node.next = new_node
            prev_node = new_node
            old1 = old1.next
            i += 1
        
        while old2:
            old2new[old2].random = old2new[old2.random]
            old2 = old2.next
        
        return old2new[head]