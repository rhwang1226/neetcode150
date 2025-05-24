from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numDict = set(nums)
        
        currentStreak = 1
        bestStreak = 0
        for num in numDict:
            if (num - 1) not in numDict:
                while (num + currentStreak) in numDict:
                    currentStreak += 1
            if currentStreak > bestStreak:
                bestStreak = currentStreak
            currentStreak = 1
        
        return bestStreak