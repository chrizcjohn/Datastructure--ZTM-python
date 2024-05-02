def merge_sorted_array(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    first_array_index, second_array_index = 0,0
    if len_arr1 ==0 or len_arr2 ==0:
        return arr1+arr2

    merge_array = []
    while first_array_index < len_arr1 and second_array_index < len_arr2:
        if arr1[first_array_index] < arr2[second_array_index]:
            merge_array.append(arr1[first_array_index])
            first_array_index += 1
        else:
            merge_array.append(arr2[second_array_index])
            second_array_index += 1

    if first_array_index == len_arr1:
        while second_array_index < len_arr2:
            merge_array.append(arr2[second_array_index])
            second_array_index += 1
    else:
        while first_array_index < len_arr2:
            merge_array.append(arr1[first_array_index])
            first_array_index += 1

    return merge_array


if __name__ == '__main__':
    arr1 = [1, 5, 20, 33, 42]
    arr2 = [5, 8, 61, 77,78,99 ]
    arr3= []
    print(merge_sorted_array(arr1, arr2))
    print(merge_sorted_array(arr1, arr3))
