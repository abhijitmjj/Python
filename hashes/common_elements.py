from typing import List

def common_elements(nums: List[List[int]]) -> List[int]:
    if not nums:
        return []

    # Start with the first subarray's elements in a set
    common_set = set(nums[0])

    # Intersect with each subsequent subarray
    for subarray in nums[1:]:
        common_set &= set(subarray)

    # Return the sorted list of common elements
    return sorted(common_set)

# Example usage
nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(common_elements(nums))  # Output: [3, 4]

# from collections import defaultdict

# class Solution:
#     def intersection(self, nums: List[List[int]]) -> List[int]:
#         counts = defaultdict(int)
#         for arr in nums:
#             for x in arr:
#                 counts[x] += 1

#         n = len(nums)
#         ans = []
#         for key in counts:
#             if counts[key] == n:
#                 ans.append(key)
        
#         return sorted(ans)