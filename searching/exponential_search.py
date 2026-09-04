# Exponential Search
# Exponential Search works only on a sorted list.
# It first finds a suitable range by increasing the index
# exponentially and then applies Binary Search on that range.

# Take sorted array input from the user
arr = list(map(int, input("Enter sorted elements: ").split()))

# Take the element to search
target = int(input("Enter element to search: "))

# Find the length of the array
n = len(arr)


# Binary Search function
def binary_search(arr, target, left, right):

    # Continue searching while the range is valid
    while left <= right:

        # Find the middle index
        mid = (left + right) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid

        # If target is greater, search in the right half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, search in the left half
        else:
            right = mid - 1

    # Target was not found
    return -1


# Handle an empty array
if n == 0:
    print("Element not found")

# Check the first element
elif arr[0] == target:
    print("Element found at index", 0)

else:
    # Start with index 1 and double it each time
    index = 1

    # Find the range where the target may exist
    while index < n and arr[index] <= target:
        index = index * 2

    # Apply Binary Search within the identified range
    left = index // 2
    right = min(index, n - 1)

    result = binary_search(arr, target, left, right)

    # Display the search result
    if result != -1:
        print("Element found at index", result)
    else:
        print("Element not found")