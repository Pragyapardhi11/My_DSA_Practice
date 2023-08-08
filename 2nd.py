# Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

# Examples:

# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#               Maximum element is: 9

# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3
#               Maximum element is: 35


def getminmax(A):
    A.sort()
    minmax={"min": A[0],"max":A[-1]}
    return minmax
A=[21,32,43,52,2,45,23]
minmax=getminmax(A)
# print("minimun element is :", minmax["min"])
# print("maximum element is :", minmax["max"])
print("minimun element is :",A[0])
print("maximum element is :",A[-1])



