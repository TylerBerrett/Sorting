# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # sets a list to the size I need and the code below replaces teh 0's with the correct numbers
    merged_arr = [0] * elements
    # TO-DO

    i = 0
    j = 0
    k = 0
    # while left or right is not empty it will compare numbers until one side is empty
    while i < len(arrA) and j < len(arrB) and k < elements:
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1

        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    # these two while loops are for grabbing the left elements on either the right side or left and adding it to the end
    # of the merged_arr
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# divide in half until you have subarrays of length 1
# sort list
# merge sorted lists together
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:

        # Splits array in half until the length of the array is 1
        half = round(len(arr) / 2)
        return merge(merge_sort(arr[:int(half)]), merge_sort(arr[int(half): len(arr)]))

    else:
        return arr


test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

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
