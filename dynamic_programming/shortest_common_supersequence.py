def shortest_common_supersequence(str1: str, str2: str) -> str:
    m, n = len(str1), len(str2)
    
    # Initialize the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the shortest common supersequence
    i, j = m, n
    scs = []
    
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            scs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] < dp[i][j - 1]:
            scs.append(str1[i - 1])
            i -= 1
        else:
            scs.append(str2[j - 1])
            j -= 1
    
    # Add remaining characters of str1 or str2
    while i > 0:
        scs.append(str1[i - 1])
        i -= 1
    while j > 0:
        scs.append(str2[j - 1])
        j -= 1
    
    # The scs list contains the characters in reverse order
    scs.reverse()
    
    return ''.join(scs)

# Example usage:
str1 = "abac"
str2 = "cab"
print(shortest_common_supersequence(str1, str2))  # Output: "cabac"