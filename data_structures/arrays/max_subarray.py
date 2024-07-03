from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize with the first element
        max_current = max_global = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)

        return max_global

# Example usage
solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))  # Output: 6
