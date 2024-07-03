from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        result = [0]*len(nums)
        
        for i in range(n - 1, -1, -1):
            
            if abs(nums[l]) < abs(nums[r]):
                res = nums[r] ** 2
                r -= 1
            else:
                res = nums[l] ** 2
                l += 1
            result[i] = res
        return result