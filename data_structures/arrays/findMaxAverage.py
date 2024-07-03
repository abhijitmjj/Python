class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for j in range(k, len(nums)):
            curr_sum += nums[j] - nums[j-k]
            max_sum = max(max_sum, curr_sum)
        return max_sum/k
        