from typing import List

def count_subarrays_with_k_odds(nums: List[int], k: int) -> int:
    def at_most_k_odds(k):
        left = 0
        count = 0
        odd_count = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
            
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            
            count += right - left + 1
        
        return count
    
    # Count subarrays with at most k odds minus at most k-1 odds
    return at_most_k_odds(k) - at_most_k_odds(k - 1)

# Example usage
nums = [1, 1, 2, 1, 1]
k = 3
print(count_subarrays_with_k_odds(nums, k))  # Output: 2
