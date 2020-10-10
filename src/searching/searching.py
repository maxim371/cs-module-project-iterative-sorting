def linear_search(arr, target):
    # Your code here
    items = len(arr)
    for item in range(0, items):
        if arr[item] == target:
            index = item
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        else:
            if arr[mid] < target:
                low = mid + 1
            if arr[mid] > target:
                high = mid - 1
    return -1  # not found
