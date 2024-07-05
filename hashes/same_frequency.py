def same_frequency(s: str) -> bool:
    from collections import Counter

    # Count the frequency of each character
    char_count = Counter(s)
    
    # Get the frequency values
    frequencies = list(char_count.values())

    # Check if all frequencies are the same
    return len(set(frequencies)) == 1

# Example usage
s1 = "abacbc"
s2 = "aaabb"
print(same_frequency(s1))  # Output: True
print(same_frequency(s2))  # Output: False

# from collections import Counter

# class Solution:
#     def areOccurrencesEqual(self, s: str) -> bool:
#         return len(set(Counter(s).values())) == 1