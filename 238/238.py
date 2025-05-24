from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = nums.count(0)

        if zeroCount > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                product *= num

        answer = []
        for num in nums:
            if zeroCount == 0:
                fraction = num ** -1
                answer.append(int(product * fraction))
            else: 
                if num == 0:
                    answer.append(product)
                else:
                    answer.append(0)

        return answer
        