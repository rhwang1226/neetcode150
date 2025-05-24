# Leetcode 242: Valid Anagram

## Robin's Solution  
### Walkthrough  
1. If the lengths of the two strings s and t are different, immediately return False — they cannot be anagrams.
2. Create two dictionaries, lettersS and lettersT, to count the frequency of each character in both strings.
3. Loop through the characters of s and t in parallel:
   - Use .setdefault(char, 0) to initialize the count if the character is not already in the dictionary.
   - Increment the count for each character in the corresponding dictionary.
4. After building both dictionaries, compare them.
   - If they are equal, return True (the strings are anagrams).
   - Otherwise, return False.

### Time Complexity  
- Loop runs n times where n = length of the string  
- Dictionary operations (setdefault, comparison) are O(1) per character  
= **O(n)**

### Space Complexity  
- Each dictionary can hold up to 26 characters (assuming only lowercase English letters)  
= **O(1)** (constant space, since the number of characters is fixed)



## Optimal Solution  
### Walkthrough  
1. Use collections.Counter to create character frequency dictionaries for both s and t.  
2. Return True if both counters are equal, otherwise return False.

### Time Complexity
Building each counter takes O(n), comparing them takes O(1) assuming bounded character set
= O(n)

### Space Complexity
Each Counter holds at most 26 entries for lowercase letters
= O(1)