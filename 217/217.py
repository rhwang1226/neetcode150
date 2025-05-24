from collections import Counter
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqDict = Counter(nums)

        for item in freqDict:
            if freqDict[item] > 1:
                return True
        
        return False
        