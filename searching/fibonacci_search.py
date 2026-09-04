# Fibonacci Search
# Fibonacci Search works only on a sorted array.
# It uses Fibonacci numbers to divide the search range
# into smaller parts.

# Take sorted array input from the user
arr = list(map(int, input("Enter sorted elements: ").split()))

# Take the element to search
target = int(input("Enter element to search: "))

# Find the length of the array
n = len(arr)

# Initialize Fibonacci numbers
fib2 = 0       # (m-2)th Fibonacci number
fib1 = 1       # (m-1)th Fibonacci number
fib = fib1 + fib2  # mth Fibonacci number

# Find the smallest Fibonacci number greater than or equal to n
while fib < n:
    fib2 = fib1
    fib1 = fib
    fib = fib1 + fib2

# Marks the eliminated range from the front
offset = -1

# Continue searching while Fibonacci number is greater than 1
while fib > 1:

    # Calculate the index to compare
    index = min(offset + fib2, n - 1)

    # If target is greater, search the right part
    if arr[index] < target:
        fib = fib1
        fib1 = fib2
        fib2 = fib - fib1
        offset = index

    # If target is smaller, search the left part
    elif arr[index] > target:
        fib = fib2
        fib1 = fib1 - fib2
        fib2 = fib - fib1

    # Target is found
    else:
        print("Element found at index", index)
        break

else:
    # Check the remaining element
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        print("Element found at index", offset + 1)
    else:
        print("Element not found")