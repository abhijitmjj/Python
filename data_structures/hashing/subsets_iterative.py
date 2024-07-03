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
def generate_subsets(nums: list[int]) -> list[list[int]]:
    """
    Explanation of the Code
    Initialization:

    generate_subsets(nums): Initializes an empty list result to store all subsets and calls the backtrack function starting from the first index.
    Backtracking Function:

    backtrack(start, current): A recursive function that generates all subsets starting from index start and using the current subset current.
    Base Case: The base case is implicitly handled by the loop termination. When start equals the length of nums, there are no more elements to consider.
    Recursive Step:

    For each element starting from start to the end of the list nums, the function explores two possibilities:
    Include: Add nums[i] to the current subset current and call backtrack recursively with the next index (i + 1).
    Exclude: Remove nums[i] from current (backtrack) and proceed to the next iteration.
    Adding Subsets:

    Every time backtrack is called, the current subset current is added to the result list result. This ensures that all subsets are captured.
    Example Usage
    For nums = [1, 2, 3], the function generates the following subsets:

    Start with an empty subset: []
    Include 1: [1]
    Include 2: [1, 2]
    Include 3: [1, 2, 3]
    Backtrack to exclude 3: [1, 2]
    Backtrack to exclude 2 and include 3: [1, 3]
    Backtrack to exclude 1 and include 2: [2]
    Include 3: [2, 3]
    Backtrack to exclude 3: [2]
    Backtrack to exclude 2 and include 3: [3]
    Backtrack to exclude 3: []"""
    def backtrack(start: int, current: list[int]) -> None:
        # Add the current subset to the result list
        result.append(current[:])
        print(f"current: {current}")
        
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current.append(nums[i])
            # Move to the next element
            backtrack(i + 1, current)
            # Exclude nums[i] from the current subset (backtrack)
            current.pop()

    result: list[list[int]] = []
    backtrack(0, [])
    return result
print(generate_subsets([1, 2, 3]))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

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
        print(f"included {k} index in subset: {subset}")
        search(k + 1, n, subset, all_subsets)

        subset.pop()
        print(f"removed {k} index from subset: {subset}")

def subsets_recursive(nums: List[int]) -> List[List[int]]:
    all_subsets: list[list[int]] = []
    search(0, len(nums), [], all_subsets)
    return all_subsets


print(subsets_recursive([1, 2, 3]))  # Output: [[], [2], [1], [1, 2], [3], [2, 3], [1, 3], [1, 2, 3]]   



# def subsets(nums: List[int]) -> List[List[int]]:
#     result: List[List[int]] = [[]]
#     for num in nums:
#         result += [curr + [num] for curr in result]
#     return result


def generate_subsets(n: int) -> list[list[int]]:
    """
    Explanation of the Python Code
    Outer Loop (for b in range(1 << n)):

    The variable b ranges from 0 to 2^n - 1.
    1 << n is equivalent to 2^n, so this loop iterates 2^n
    times, generating all possible subsets.

    Inner Loop (for i in range(n)):

    For each value of b, this loop checks each bit position i from 0 to n-1.
    Bit Check (if b & (1 << i)):

    1 << i creates a number with only the  i-th bit set.
    b & (1 << i) checks if the  i-th bit in b is set.
    If the i-th bit is set, it means the i-th element is included in the current subset.
    Subset Construction (subset.append(i)):

    If the bit check is true, the i-th element is added to the current subset.
    Collecting All Subsets (all_subsets.append(subset)):

    Each generated subset is added to the list all_subsets."""
    all_subsets: list[list[int]] = []
    for b in range(1 << n):  # Iterate over all possible subsets
        subset: list[int] = []
        for i in range(n):  # Check each bit position
            if b & (1 << i):  # If the ith bit is set, include i in the subset
                subset.append(i)
        all_subsets.append(subset)
    return all_subsets

# Example usage
n = 3
subsets = generate_subsets(n)
print(subsets)  # Output: [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]

def generate_subsets(nums: list[Any]) -> list[list[Any]]:
    n = len(nums)
    all_subsets: list[list[Any]] = []
    
    for b in range(1 << n):  # Iterate over all possible subsets (2^n subsets)
        subset = [nums[i] for i in range(n) if b & (1 << i)]  # Use list comprehension to build the subset
        all_subsets.append(subset)
    
    return all_subsets

# Example usage
nums = [1, 2, 3]
subsets = generate_subsets(nums)
print(subsets)

def binary_and(str1: str, str2: str) -> str:
    # Remove '0b' prefix and ensure equal lengths
    str1 = str1[2:].zfill(max(len(str1), len(str2)) - 2) 
    str2 = str2[2:].zfill(max(len(str1), len(str2)) - 2)

    result = ""
    for i in range(len(str1)):
        result += '1' if str1[i] == '1' and str2[i] == '1' else '0'
    return '0b' + result

combined_binary = binary_and(bin(1), bin(1 << 2))
print(combined_binary)  # Output: 0b0
