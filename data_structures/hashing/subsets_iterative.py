from typing import Any, List


# Base Case:

# If k equals n, it means we have considered all elements, and we process the current subset.
# Recursive Case:

# The function search(k + 1) is called without including the current element k in the subset.
# The element k is then added to the subset, and search(k + 1) is called again to include the current element in the subset.
# After processing the subset including the current element, it is removed (subset.pop_back()) to backtrack.

# void search(int k) {
#     if (k == n) {
#         // process subset
#     } else {
#         search(k + 1);
#         subset.push_back(k);
#         search(k + 1);
#         subset.pop_back();
#     }
# }

def search(k: int, n: int, subset: list[Any], all_subsets: list[list[Any]]):
    """
    :param k: current index
    :param n: length of nums
    :param subset: current subset
    :param all_subsets: all subsets
    
    When the function search is called with parameter k, it decides whether to
    include the element k in the subset or not, and in both cases, then calls itself
    with parameter k + 1 However, if k = n, the function notices that all elements
    have been processed and a subset has been generated.
    The following tree illustrates the function calls when n = 3. We can always
    choose either the left branch (k is not included in the subset) or the right branch
    (k is included in the subset).
    """
    if k == n:
        # process subset
        all_subsets.append(subset[:])
    else:
        # The function search(k + 1) is called without including the current element k in the subset.
        search(k + 1, n, subset, all_subsets)
        # Include nums[k] in the subset
        # The element k is then added to the subset, and search(k + 1) is called again to include the current element in the subset.
        subset.append(k)
        search(k + 1, n, subset, all_subsets)

        subset.pop()

def subsets_recursive(nums: List[int]) -> List[List[int]]:
    all_subsets = []
    search(0, len(nums), [], all_subsets)
    return all_subsets


print(subsets_recursive([1, 2, 3]))  # Output: [[], [2], [1], [1, 2], [3], [2, 3], [1, 3], [1, 2, 3]]   



# def subsets(nums: List[int]) -> List[List[int]]:
#     result: List[List[int]] = [[]]
#     for num in nums:
#         result += [curr + [num] for curr in result]
#     return result


# def subsets_bitmask(nums: List[int]) -> List[List[int]]:
#     n = len(nums)
#     result = []
#     for i in range(1 << n):
#         subset = []
#         for j in range(n):
#             if i & (1 << j):
#                 subset.append(nums[j])
#         result.append(subset)
#    return result