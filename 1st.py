# Given an array (or string), the task is to reverse the array/string.
# Examples : 
 

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}




def reverselist(A,start,end):
    while start < end:
        A[start],A[end] = A[end],A[start]
        start=start+1
        end = end-1

A =[1,2,5,78,34,65]
print(A)
reverselist(A,0,5)
print("reverse list is:")
print(A)        