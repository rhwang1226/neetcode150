# Leetcode 49: Group Anagrams

## Robin's Solution  
**Note**: This is a valid solution but times out on Leetcode.
### Walkthrough  
1. Define a helper function `isAnagram(s, t)` that returns `True` if two strings are anagrams by comparing their character frequency dictionaries.  
2. Use a dictionary `wordDict` where each key is a representative anagram and the value is a list of strings belonging to that group.  
3. Iterate through the input list `strs`, and for each string, check against every key in `wordDict` using `isAnagram`.  
4. If an anagram group is found, append the string to the corresponding list. Otherwise, add it as a new key-value pair.  
5. At the end, return the values of `wordDict` as the grouped anagrams.

### Time Complexity  
Let:  
- n = number of strings  
- k = average length of each string  
- m = number of unique anagram groups  
- `isAnagram` takes O(k) time to count letters and compare maps (technically O(k) + O(26) = O(k))  

Each string is compared with up to m keys in the dictionary = **O(n * m * k)** in the worst case.  

### Space Complexity  
- Up to O(n * k) space for storing character counts in each dictionary call.  
- Final result is also O(n * k) for holding all input strings grouped = **O(nk)** total.


## Optimal Solution  
### Walkthrough  
1. Instead of comparing strings directly, sort each string (or use a tuple of character counts as a hashable key).  
2. Use a dictionary to group strings by their sorted string or count tuple.  
3. Append each original string to the correct list in the dictionary.  
4. Return the dictionary’s values as the grouped anagrams.

### Time Complexity  
Sorting each string takes O(k log k), and you do it for all n strings = **O(n * k log k)**  
→ Much faster than comparing each pair.

### Space Complexity  
- Dictionary holds all strings grouped = **O(nk)**  
- If sorting strings, temporary sorted versions take up space = still **O(nk)** total.
