# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# divide in half until you have subarrays of length 1
# sort list
# merge sorted lists together
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

        if len(arr) == 3:
            if arr[1] > arr[2]:
                arr[1], arr[2] = arr[2], arr[1]
                if arr[1] < arr[0]:
                    arr[0], arr[1] = arr[1], arr[0]

        half = len(arr) / 2
        return merge(merge_sort(arr[:int(half)]), merge_sort(arr[int(half): len(arr)]))

    else:
        return arr


test = [4, 1, 53, 89, 46, 33, 14, 56, 98, 123]

print(merge_sort(test))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
