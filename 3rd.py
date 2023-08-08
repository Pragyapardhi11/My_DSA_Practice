# Given an array arr[] and an integer K where K is smaller than size of array, the task is 
# to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Note :-  l and r denotes the starting and ending index of the array.


def minmax(A):
    A.sort()
    # A[0]=s
    # A[-1]=l
    print(A)

A=[78,56,4,8,9]
minmax(A)
k=int(input("which smallest no. you want:"))
print(A[k-1])
# p=int(input("which highest no. you want:"))
# print(A[-k])
