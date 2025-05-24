# Leetcode 128: Longest Consecutive Subsequence

## Robin's Solution
### Walkthrough
1. Copy the list into a set and initialize variables to keep track of longest so far and current subsequence length.
2. Iterate through the set. If num - 1 is not in the set, that means num is the start of a subsequence and we should start iterating through num + 1, num + 2, etc... using a while loop to check if these are in the set as well.
3. If num + currentStreak is in the set, it should iterate currentStreak and keep doing so until this is not the case.
4. Update the longest so far (bestStreak) variable as necessary and reset currentStreak to 1.

### Time Complexity
O(n) to iterate through the number dict. For the while loop, the worst case of a consecutive array (ie: [1,2,3,4,5]) will only be O(n) at most once. This is because when the program detects the first number, it will execute the O(n) while loop, but then it is impossible for it to execute the while loop for the rest of numbers since we have that check for num - 1 in the set.

### Space Complexity
O(n) to copy the list into a new dict

## Optimal Solution
Robin's solution is optimal already.