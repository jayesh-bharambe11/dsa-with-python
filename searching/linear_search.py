# Linear Search

# Take array input from user
arr = list(map(int, input("Enter elements: ").split()))

# Take the element to search
target = int(input("Enter element to search: "))

# Check each element one by one
for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        break
else:
    print("Element not found")