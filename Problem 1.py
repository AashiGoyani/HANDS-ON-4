def Sorted_Array(arr):
    if not arr:
        return []

    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_half = Sorted_Array(arr[:mid])
    right_half = Sorted_Array(arr[mid:])
    
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

array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]
arr = [array1, array2, array3]

result = Sorted_Array(arr)
print(result)
