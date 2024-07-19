def shortest_common_supersequence(str1: str, str2: str) -> str:
    """Shortest Common super sequence To solve the problem of finding the shortest
    common supersequence (SCS) of two given strings, we can use dynamic programming. The
    shortest common supersequence of two strings is the shortest string that has both
    strings as subsequences.

    Steps:

            1.      Find the Length of SCS:
                •   Use dynamic programming to find the length of the shortest common supersequence.
                •   Construct a 2D array dp where dp[i][j] represents the length of the shortest common supersequence of str1[0..i-1] and str2[0..j-1].
            2.      Reconstruct the SCS:
                •   Use the dp table to reconstruct the actual shortest common supersequence.

        Dynamic Programming Approach

            1.      Initialize the DP Table:
                •   If one of the strings is empty, the length of the SCS is the length of the other string.
            2.      Fill the DP Table:
                •   If characters of both strings match, then the SCS length is 1 + dp[i-1][j-1].
                •   If characters do not match, then the SCS length is 1 + min(dp[i-1][j], dp[i][j-1]).
            3.      Reconstruct the SCS:
                •   Start from dp[m][n] and trace back to dp[0][0] to construct the SCS.
    """
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
    scs: list[str] = []

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

    return "".join(scs)


# Example usage:
str1 = "abac"
str2 = "cab"
print(shortest_common_supersequence(str1, str2))  # Output: "cabac"
