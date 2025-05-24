import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}

        for i in range(len(nums)):
            numDict.setdefault(nums[i], 0)
            numDict[nums[i]] += 1

        return heapq.nlargest(k, numDict.keys(), key=numDict.get)
    