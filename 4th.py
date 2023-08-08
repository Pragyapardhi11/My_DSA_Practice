# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# You don't need to read input or print anything. Your task is to complete the function sort012()
# that takes an array arr and N as input parameters and sorts the array in-place.


def sort012(arr):
    arr.sort()
    print(arr)
    
arr=[2,0,1,2,1,0,1,0,1,2,]
sort012(arr)


