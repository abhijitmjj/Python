from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts:dict[int, int] = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
    
        return ans
    
# Example usage
nums = [1, 1, 1]
k = 2
print(Solution().subarraySum(nums, k))  # Expected: 2
nums = [1, 2, 3]
k = 3
print(Solution().subarraySum(nums, k))  # Expected: 2
nums = [1, 2, 1, 2, 1]
k = 3
print(Solution().subarraySum(nums, k))  # Expected: 4
nums = [1, -1, 1, -1]
k = 0
print(Solution().subarraySum(nums, k))  # Expected: 4