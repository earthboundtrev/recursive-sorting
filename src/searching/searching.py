import math
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    mid = math.floor(((end+start)/2))

    if start == end+1:
        return -1

    if mid == end-1 or start+1 == mid:
        return mid
    else:
        if(target < arr[mid]):
            end = mid
        elif(target == arr[mid]):
            return mid
        else:
            start = mid
        return binary_search(arr, target, start, end)

    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass

