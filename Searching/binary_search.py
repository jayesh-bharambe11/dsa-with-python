# Binary Search
# Binary Search works only on a sorted list.
# It repeatedly divides the search range into two halves.

# Take sorted array input from the user
arr = list(map(int, input("Enter sorted elements: ").split()))

# Take the element to search
target = int(input("Enter element to search: "))

# Set the starting and ending positions
low = 0
high = len(arr) - 1

# Continue searching while the range is valid
while low <= high:

    # Find the middle index
    mid = (low + high) // 2

    # Check if the middle element is the target
    if arr[mid] == target:
        print("Element found at index", mid)
        break

    # If target is greater, search in the right half
    elif arr[mid] < target:
        low = mid + 1

    # If target is smaller, search in the left half
    else:
        high = mid - 1

# This runs if the loop finishes without finding the target
else:
    print("Element not found")