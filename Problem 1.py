def sorted_array_merge(arrays):
    if not arrays:
        return []

    if len(arrays) == 1:
        return arrays[0]

    mid = len(arrays) // 2
    left_half = sorted_array_merge(arrays[:mid])
    right_half = sorted_array_merge(arrays[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Getting the number of arrays and size of each array from the user
num_arrays = int(input("Enter the number of arrays: "))
size_of_arrays = int(input("Enter the size of each array: "))

# Sorting input array from user
arrays = []
for _ in range(num_arrays):
    array_input = input(f"Enter array elements separated by space: ")
    array = list(map(int, array_input.split()))
    arrays.append(sorted(array))
print(arrays)

result = sorted_array_merge(arrays)
print("Result:", result)



#EXAMPLE

# Enter the number of arrays: 3
# Enter the size of each array: 4
# Enter array elements separated by space: 3 5 2 7
# Enter array elements separated by space: 8 7 9 2
# Enter array elements separated by space: 7 3 8 3
# [[2, 3, 5, 7], [2, 7, 8, 9], [3, 3, 7, 8]]
# Result: [2, 2, 3, 3, 3, 5, 7, 7, 7, 8, 8, 9]
