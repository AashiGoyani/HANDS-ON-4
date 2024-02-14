def remove_duplicates(arr):
    if not arr:
        return arr

    set1 = set()
    final_array = []

    for i in arr:
        if i not in set1:
            final_array.append(i)
            set1.add(i)

    return final_array


array1 = [2, 2, 2, 2, 2]
output1 = remove_duplicates(array1)
print("Input Array: ", array1)
print("Output Array: ", output1)

array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
output2 = remove_duplicates(array2)
print("Input Array: ", array2)
print("Output Array: ", output2)
