# Leetcode 217: Contains Duplicate


## Robin's Solution
### Walkthrough
1. Use Counter (from collections library) to create a dictionary that stores list items and their frequencies.
2. Iterate through the dictionary and check if any key holds a value (representing frequency) greater than 1. If yes, return True. At the end of the loop, if no value greater than 1 found, return False.
### Time Complexity
O(n) to use Counter (copying list items to dict), O(n) to iterate through dictionary, O(1) to check the key's value (dict support O(1) search) = O(2n + 1) = **O(n)**
### Space Complexity
Creating the dictionary results in **O(n)**.


## Optimal Solution
### Walkthrough
1. Create empty set to hold "seen" items.
2. Iterate through the list and check if the current int is in the set. If it is, return True. If not, add the item to the set and continue to iterate. At the end of the loop, return False (no duplicates found).
### Time Complexity
Creating an empty set is O(1), iterating through the list is O(n), O(1) to lookup current item in the set (set is implemented with dictionary so it supports constant search) = O(n + 2) = **O(n)**
### Space Complexity
Set is **O(n)** (holds n-1 elements for case where duplicate item is in the last index of the list)