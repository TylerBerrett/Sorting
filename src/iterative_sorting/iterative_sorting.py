# TO-DO: Complete the selection_sort() function below
import random
def selection_sort(arr):
    # loop through n-1 elements, why?
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        smallest_num = arr[smallest_index]
        position = arr[cur_index]
        arr[smallest_index] = position
        arr[cur_index] = smallest_num

        # TO-DO: swap

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Compare one element with the one to the right of it until I hit the end
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


print(bubble_sort([0, 3, 14, 2, 123]))
# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
