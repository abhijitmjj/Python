def length_of_longest_substring_k_distinct(s: str, k: int) -> int:

    """
    Given a string s, find the length of the longest substring that contains at most k distinct characters.
    """
    from collections import defaultdict
    if k == 0:
        return 0

    left, right = 0, 0
    max_length = 0
    char_count = defaultdict(int)
    for right, c in enumerate(s):
        char_count[c] += 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)
    
    return max_length

if __name__ == "__main__":
    print(length_of_longest_substring_k_distinct("eceba", 2))  # Expected: 3
    print(length_of_longest_substring_k_distinct('aa', 1))  # Expected: 2
    import doctest
    doctest.testmod()

