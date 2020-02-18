# TO-DO: Complete the selection_sort() function below
import random
def selection_sort(arr):
    # goes up till the length of the array ex: if len(arr) = 12 i will only go up to 11
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # loops through all the values of the array starting from the current index and finds the smallest value and
        # sets the smallest_index variable to the index of that number
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # swaps places with where the the number at the current index is with the smallest number
        smallest_num = arr[smallest_index]
        position = arr[cur_index]
        arr[smallest_index] = position
        arr[cur_index] = smallest_num

        # TO-DO: swap
    print(arr)
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Compare one element with the one to the right of it until I hit the end
    # keep track if something was swapped then loop again
    # loop until no swaps happen
    check_swap = True
    while check_swap:
        did_swap = 0
        # compares the element with the one to the right of it and if the element is larger than the one on the right
        # then swap elements and add to did_swap to let the while loop know that we are not done yet
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                did_swap += 1

        # notifies the while loop to stop if no swaps were preformed
        if did_swap == 0:
            check_swap = False
    print(arr)
    return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
