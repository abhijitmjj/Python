def getAverages(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    avgs = [-1] * n
    if 2 * k + 1 > n:
        return avgs

    # Calculate prefix sums
    # Why n + 1? To simplify the sum of elements from the start of the array up to any given point without having to handle special cases.
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # Calculate k-radius averages
    for i in range(k, n - k):
        # The sum of elements from the start of the array up to i + k + 1 minus the sum of elements from the start of the array up to i - k
        total_sum = prefix_sum[i + k + 1] - prefix_sum[i - k]
        avgs[i] = total_sum // (2 * k + 1)

    return avgs