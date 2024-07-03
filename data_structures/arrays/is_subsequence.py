
def is_subsequence(s: str, t: str) -> bool:
    """
    Check if a string is a subsequence of another string. (skip characters in between - allowed)
    :param s: string
    :param t: string
    :return: bool
    """

    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            # advance the pointer of the subsequence string
            i += 1
        # advance the pointer of the main string
        j += 1
    return i == len(s)

if __name__ == '__main__':
    print(is_subsequence("ace", "abcde"))  # Output: True