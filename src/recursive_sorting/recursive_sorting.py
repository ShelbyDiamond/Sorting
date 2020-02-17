# TO-DO: complete the help function below to merge 2 sorted arrays
import math

def merge_sort(arr):
    if(len(arr)<1):
        return [];
    return merge_arrays([], split_array(arr))

def split_array(arr):
    if(len(arr)<=1):
        return [arr]

    half = math.ceil(len(arr)/2)
    return split_array(arr[half:]) + split_array(arr[:half])

def merge_arrays(sorted, split):
    if(len(split) == 0):
        return sorted

    item = split.pop(0)[0]
    if(len(sorted) == 0 or sorted[len(sorted)-1] <= item):
        sorted.append(item)
    else:
        for i in range(len(sorted)):
            if sorted[i] >= item:
                sorted.insert(i,item)
                break
    return merge_arrays(sorted, split)

print(merge_sort([])) # [1, 4, 5, 8, 9, 13, 16, 21, 55]

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # Due to time constraints, I think I'm leaving this one alone :(
    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    # So I've done a bit of research and doing a legit timsort looks like more of a weekend project than something I can accomplish in one night.
    # There's a lot of logic involved and since I'll be gone for a lot of tomorrow, I'm going to put this aside for now and come back to it later.

    return arr