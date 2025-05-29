def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # find the middle index
        if arr[mid] == target:
            return mid  # found the target
        elif arr[mid] < target:
            low = mid + 1  # search in the right half
        else:
            high = mid - 1  # search in the left half

    return -1  # target not found
arr = [2, 4, 7, 10, 14, 18, 25]
target = 14

index = binary_search(arr, target)
print("Target found at index:", index)  # Output: Target found at index: 4
