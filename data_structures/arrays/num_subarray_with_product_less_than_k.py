def num_subarrays_with_product_less_than_k(arr: list[int], k: int) -> int:
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right in range(len(arr)):
        product *= arr[right]

        while product >= k and left <= right:
            product /= arr[left]
            left += 1

        count += right - left + 1

    return count

# Example usage
arr = [10, 5, 2, 6]
k = 100
print(num_subarrays_with_product_less_than_k(arr, k))  # Output: 8
