# Jump Search
# Jump Search works only on a sorted list.
# It searches by jumping fixed-size blocks and then
# performing a linear search within the required block.

import math

# Take sorted array input from the user
arr = list(map(int, input("Enter sorted elements: ").split()))

# Take the element to search
target = int(input("Enter element to search: "))

# Store the length of the array
n = len(arr)

# Calculate the optimal jump size (square root of array length)
jump = int(math.sqrt(n))

# Set the starting index of the current block
left = 0

# Set the ending index of the current block
right = jump

# Find the block where the target may exist
while left < n and arr[min(right, n) - 1] < target:
    left = right
    right += jump

    # If the starting index goes beyond the array
    if left >= n:
        break

# Perform linear search within the identified block
while left < min(right, n):

    # Check if the current element is the target
    if arr[left] == target:
        print("Element found at index", left)
        break

    # Move to the next element
    left += 1

else:
    print("Element not found")