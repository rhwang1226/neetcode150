# Leetcode 347: Top K Frequent Elements

## Robin's Solution  
### Walkthrough  
1. Create an empty dictionary `numDict` to store frequencies of each number in the list.  
2. Iterate through the `nums` array:  
   - Use `.setdefault(num, 0)` to initialize the count.  
   - Increment the count for each number encountered.  
3. Use Python’s `heapq.nlargest()` function to return the `k` keys with the highest frequencies.  
   - Pass `numDict.get` as the key function to sort by frequency.

### Time Complexity  
- Building the frequency dictionary takes O(n), where `n` = length of `nums`.  
- `heapq.nlargest()` on `m` unique elements takes O(m log k).  
  Let `m` = number of unique elements  
= **O(n + m log k)**

### Space Complexity  
- Dictionary stores up to `m` entries = O(m)  
- Heap stores `k` elements = O(k)  
= **O(m + k)**


## Optimal Solution
Robin's solution is optimal already.