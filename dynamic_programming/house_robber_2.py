from functools import lru_cache
from typing import List, Tuple

# def rob(nums: List[int]) -> Tuple[int, List[int]]:
#     n = len(nums)
#     if n == 0:
#         return 0, []
#     if n == 1:
#         return nums[0], [0]
    
#     # Memoization using lru_cache
#     @lru_cache(maxsize=None)
#     def dp(i: int) -> int:
#         if i == 0:
#             return nums[0]
#         if i == 1:
#             return max(nums[0], nums[1])
#         return max(dp(i - 1), dp(i - 2) + nums[i])
    
#     max_amount = dp(n - 1)
    
#     # Reconstruction of the solution
#     rob_sequence: list[int] = []
#     i = n - 1
#     while i >= 0:
#         # we start from the last element and move backwards to find the sequence
#         if i == 0 or (i == 1 and dp(1) == nums[1]) or (i > 1 and dp(i) == dp(i - 2) + nums[i]):
#             rob_sequence.append(i)
#             i -= 2
#         else:
#             i -= 1
    
#     rob_sequence.reverse()
#     return max_amount, rob_sequence

from typing import List, Tuple
def rob(nums: list[int]) -> Tuple[int, list[int]]:
    if not nums:
        return 0, []
    n = len(nums)
    if n == 1:
        return nums[0], [0]
    if n == 2:
        return max(nums[0], nums[1]), [0] if nums[0] > nums[1] else [1]
    
    dp: list[tuple[int, list[int]]] = [(0, []) for _ in range(n)]
    dp[0] = nums[0], [0]
    dp[1] = max(nums[0], nums[1]), [0] if nums[0] > nums[1] else [1]
    
    for i in range(2, n):
        dp[i] = max(dp[i-1][0], dp[i-2][0] + nums[i]), dp[i-1][1] if dp[i-1][0] > dp[i-2][0] + nums[i] else dp[i-2][1] + [i]
    
    return dp[-1]

def rob_circle(nums: list[int]) -> tuple[int, list[int]]:
    if len(nums) == 0:
        return 0, []
    if len(nums) == 1:
        return nums[0], [0]
    if len(nums) == 2:
        return max(nums[0], nums[1]), [0] if nums[0] > nums[1] else [1]
    
    rob_first_skip_last = rob(nums[:-1])
    rob_second_skip_first = rob(nums[1:])
    # adjust the index of the second solution
    rob_second_skip_first_mod = (rob_second_skip_first[0], [i + 1 for i in rob_second_skip_first[1]])
    return max(rob_first_skip_last, rob_second_skip_first_mod, key=lambda x: x[0])



# Example usage:
nums = [2, 7, 9, 3, 1]*20
max_amount, rob_sequence = rob(nums)
print("Max amount:", max_amount)  # Expected output: 12
print("Rob sequence:", rob_sequence)  # Expected output: [1, 3]