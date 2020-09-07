import math
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    mid = math.floor(((end+start)/2))

    if len(arr)==0:
        return -1

    else:
        if(target < arr[mid]):
            return binary_search(arr, target, start, mid)
        elif(target == arr[mid]):
            return mid
        else:
            return binary_search(arr, target, mid, end)

    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass

