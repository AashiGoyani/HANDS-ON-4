def Sorted_Array1(arr):
    if not arr:
        return []

    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_half = Sorted_Array1(arr[:mid])
    right_half = Sorted_Array1(arr[mid:])
    
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

result = Sorted_Array1(arr)
print("Result 1: ",result)

#-----------------------------------------------------------------------------------------------------------#

def Sorted_Array2(arrays):
    if not arrays:
        return []

    if len(arrays) == 1:
        return arrays[0]

    mid = len(arrays) // 2
    left_half = Sorted_Array2(arrays[:mid])
    right_half = Sorted_Array2(arrays[mid:])
    
    return merge(left_half, right_half)

def merge(left1, right1):
    result2 = []
    a = b = 0

    while a < len(left1) and b < len(right1):
        if left1[a] < right1[b]:
            result2.append(left1[a])
            a += 1
        else:
            result2.append(right1[b])
            b += 1

    result2.extend(left1[a:])
    result2.extend(right1[b:])

    return result2

array4 = [1,3,7]
array5 = [2,4,8]
array6 = [9,10,11]
arrays = [array4, array5, array6]

result2 = Sorted_Array2(arrays)
print("Result 2: ",result2)



