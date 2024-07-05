

def repeatedCharacter(s: str) -> str:
        """
        Given a string s, return the first character to appear twice.
        It is guaranteed that the input will have a duplicate character.
        """
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "

# Test cases


if __name__ == "__main__":
    print(repeatedCharacter('Algorithms'))  # Expected: g
    print(repeatedCharacter('go adler em all'))  # Expected: a
    import doctest
    doctest.testmod()