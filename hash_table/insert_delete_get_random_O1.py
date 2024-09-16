"""
380. Insert Delete GetRandom O(1) (Medium)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""

import random


class RandomizedSet:
    """Runtime: 432 ms"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_list:
            return False
        self.val_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.val_list:
            self.val_list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.val_list)


import random


class RandomizedSet:
    """Runtime: 96 ms"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val2idx = {}
        self.val_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.val2idx:
            self.val2idx[val] = len(self.val_list)
            self.val_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.val2idx:
            idx, last_element = self.val2idx[val], self.val_list[-1]
            self.val_list[idx] = last_element
            self.val2idx[last_element] = idx

            self.val_list.pop()
            del self.val2idx[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.val_list)
