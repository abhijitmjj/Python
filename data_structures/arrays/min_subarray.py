from typing import List

class Solution:
    def minSubArray(self, nums: List[float]) -> float:
        # Initialize with the first element
        min_current = min_global = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            min_current = min(num, min_current + num)
            min_global = min(min_global, min_current)

        return min_global

# Example usage
solution = Solution()
nums = [1.1, -2.3, 3.4, -4.5, 5.6, -6.7]
print(solution.minSubArray(nums))  # Output: -6.7
