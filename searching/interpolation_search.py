# Interpolation Search
# Interpolation Search works only on a sorted array.
# It estimates the probable position of the target
# instead of always checking the middle element.

# Take sorted array input from the user
arr = list(map(int, input("Enter sorted elements: ").split()))

# Take the element to search
target = int(input("Enter element to search: "))

# Set the starting index
low = 0

# Set the ending index
high = len(arr) - 1

# Continue searching while the target is within the range
while low <= high and arr[low] <= target <= arr[high]:

    # If both values are equal, check the first position
    if arr[low] == arr[high]:
        if arr[low] == target:
            print("Element found at index", low)
        else:
            print("Element not found")
        break

    # Estimate the probable position of the target
    position = low + (
        (target - arr[low]) * (high - low)
        // (arr[high] - arr[low])
    )

    # Check if the target is found
    if arr[position] == target:
        print("Element found at index", position)
        break

    # If target is greater, search in the right part
    elif arr[position] < target:
        low = position + 1

    # If target is smaller, search in the left part
    else:
        high = position - 1

else:
    # Target was not found
    print("Element not found")