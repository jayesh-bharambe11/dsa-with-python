# Ternary Search
# Ternary Search works only on a sorted array.
# It divides the search range into three parts
# and checks the two middle positions.

# Take sorted array input from the user
arr = list(map(int, input("Enter sorted elements: ").split()))

# Take the element to search
target = int(input("Enter element to search: "))

# Set the starting index
left = 0

# Set the ending index
right = len(arr) - 1

# Continue searching while the range is valid
while left <= right:

    # Divide the range into three parts
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    # Check the first middle position
    if arr[mid1] == target:
        print("Element found at index", mid1)
        break

    # Check the second middle position
    elif arr[mid2] == target:
        print("Element found at index", mid2)
        break

    # Target is in the left third
    elif target < arr[mid1]:
        right = mid1 - 1

    # Target is in the right third
    elif target > arr[mid2]:
        left = mid2 + 1

    # Target is in the middle third
    else:
        left = mid1 + 1
        right = mid2 - 1

else:
    # Target was not found
    print("Element not found")