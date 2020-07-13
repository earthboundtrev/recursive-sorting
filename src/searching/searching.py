import math
# import ipdb
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    mid = math.floor(((end+start)/2))

    if start == end+1:
        return -1

    # ipdb.set_trace()
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

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# binary_search(arr1, 0, 0, len(arr1)-1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass

