# Leetcode 238: Product of Array Except Self

## Robin's Solution  
### Walkthrough  
1. Count how many zeroes are in the list (zeroCount).
2. If more than one zero exists, return a list of all zeroes — any product excluding self will always be zero.
3. Calculate the total product of all non-zero elements.
4. Iterate through the array again:
   - If no zero in the list, use product * (1 / num) for each element.
   - If there is one zero:
     - Put product at the zero’s position (since it’s the product of all other non-zero elements).
     - Place 0 elsewhere.

### Time Complexity  
- O(n) to count zeros  
- O(n) to compute the product  
- O(n) to build the output list  
= **Total: O(n)**

### Space Complexity  
- Output list takes O(n) space  
- Constant extra space otherwise  
= **O(n)**

---

## Optimal Solution (Without Division)  
### Walkthrough  
1. Use two passes:
   - In the first pass, calculate the prefix product for each index.
   - In the second pass (from right to left), multiply the running suffix product into the result.
2. Avoids division and handles zeros implicitly.

### Time Complexity  
Two full passes that are O(n) each = **O(n)**

### Space Complexity  
Output list is O(n), All other variables are O(1), **O(n) total (but O(1) extra space**, since output doesn't count as extra)