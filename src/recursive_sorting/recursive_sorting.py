# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# divide in half until you have subarrays of length 1
# merge sorted lists together
# index 1 = right, 0 = left
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        half = len(arr) / 2
        return merge_sort(arr[0: int(half)]), merge_sort(arr[int(half): len(arr)])
    else:
        return arr


test = [1, 4, 12, 89, 46, 12, 14, 56, 98, 123]

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
