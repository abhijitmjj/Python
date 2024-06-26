def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Merge two sorted arrays into a single sorted array.
    """

    i = j = 0
    result = []
    
    while i < len(arr1) and j < len(arr2):

        if (arr1[i] < arr2[j]):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    # one of the lists will reach the end first
    # so we need to add the remaining elements of the other list
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

if __name__ == '__main__':
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    print(merge(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print(merge(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 4]
    print(merge(arr1, arr2))  # Output: [1, 1, 2, 2, 3, 3, 4, 4]
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8, 9]
    print(merge(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr1 = [5, 6, 7, 8, 9]
    arr2 = [1, 2, 3, 4]
    print(merge(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(merge(arr1, arr2))  # Output: [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]
