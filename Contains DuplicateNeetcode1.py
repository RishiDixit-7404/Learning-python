from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        i = 0
        while i < len(nums):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count = 1 
                    break    
            if count == 1:
                break      
            i += 1

        if count == 0:
            return False  
        else:
            return True    
a = list(range(0,10))
sol = Solution()
print(sol.hasDuplicate(a))