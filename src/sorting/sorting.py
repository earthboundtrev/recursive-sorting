# import ipdb
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    second_addition_size = elements - len(arrB)

    # Your code here
    # ipdb.set_trace()
    counter = 0
    for i in range(0, len(arrA)):
        merged_arr[i] = arrA[i]
        counter = counter+1
    for j in range(0, len(arrB)):
        merged_arr[counter] = arrB[j]
        counter = counter+1

    for i in range(0, (len(merged_arr))):
        for j in range(0, (len(merged_arr))):
            if merged_arr[i] < merged_arr[j]:
                temp_variable = merged_arr[i]
                merged_arr[i] = merged_arr[j]
                merged_arr[j] = temp_variable

    return merged_arr
arrB=[0,2,4]
arrA = [1,3,5]

print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    start = 0
    end = len(arr)-1
    mid = ((start+end/2))

    new_list1=[]
    new_list2=[]


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

