# import ipdb
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    starting_point = 0
    counter = 0
    for i in range(0, len(arrA)):
        # ipdb.set_trace()
        if(counter >= elements):
            counter = 0
        for j in range(0, len(arrB)):

            print("Merged_arr value:", merged_arr[starting_point])
            counter=counter+1
            print("This is the counter:", counter)
            print("Counter value:", counter, "arr[A] value:", arrA[i], "arr[B] value:", arrB[j])
            if counter == len(arrB):
                starting_point=starting_point+1
                print("This is the starting_point: ", starting_point)

            if(arrA[i] < arrB[j]):
                merged_arr[starting_point] = arrA[i]
            else:
                merged_arr[starting_point] = arrB[j]
                


    return merged_arr
arrA = [2,3,4]
arrB = [5,6,7]

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

