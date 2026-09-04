# Binary Search
# Binary Search works only on a sorted list.
# It searches by repeatedly dividing the list into two halves.

# Take sorted array input from the user
arr = list(map(int, input("Enter sorted elements: ").split()))

# Take the element to search
target = int(input("Enter element to search: "))

# Set the starting index
low = 0

# Set the ending index
high = len(arr) - 1

# Continue searching while the search range is valid
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

# If the target was not found
else:
    print("Element not found")