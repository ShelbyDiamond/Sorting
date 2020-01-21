# TO-DO: Complete the selection_sort() function below

my_list_a = [7, 4, 6, 1, 7, 2, 76, -250]
my_list_b = [436, 22, 2, 90, 23, 19, -7]

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): # O(n)
        cur_index = i
        smallest_index = cur_index

        # After first iteration, smallest should be on left side of the list.
        # So we can start counting from wherever 'i' is (and thus compare to i+1)
        for j in range(i+1, len(arr)): # O(n)
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr# --> O(n^2)


print(selection_sort(my_list_a))
print(selection_sort(my_list_b))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # The highest number will always end up at the end after each iteration through the list
    # Thus, after each iteration I can check one fewer index.  Easiest way to do this is
    # Have one loop count at the end, down to the front while the other loop counts from 0
    # to the parent loop's counter variable
    for i in range(len(arr)-1, 0, -1):  # O(n)
        for j in range(0, i):  # O(n)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr # O(n^2)

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr