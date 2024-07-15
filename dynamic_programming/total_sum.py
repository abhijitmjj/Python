def totalSum(inp: list[int], target: int) -> tuple[int, list[list[int]]]:
    # Initialize dp where each element is a tuple:
    # First element is the count of ways to make the sum
    # Second element is the list of all combinations to make the sum
    dp = [(0, []) for _ in range(target + 1)]
    dp[0] = (1, [[]])  # There is one way to make 0: using no coins

    for i in range(1, target + 1):
        all_combinations = []  # List to hold all combinations for the current i
        total_ways = 0  # Counter to count total ways to form the current i
        for coin in inp:
            if i - coin >= 0:
                total_ways += dp[i - coin][0]  # Add ways from the sub-problem
                for comb in dp[i - coin][1]:
                    new_comb = comb + [coin]  # Form a new combination
                    all_combinations.append(new_comb)
        dp[i] = (total_ways, all_combinations)

    return dp

if __name__ == "__main__":
    inp = [2, ]
    target = 3
    result = totalSum(inp, target)
    print(result)
    # print(f"Total ways: {result[0]}, Combinations: {result[1]}")
