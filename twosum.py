target = 7
nums = [3,4,5,6]
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]== target:
         print(f"[{i},{j}]")

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}  # number to index mapping
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i

