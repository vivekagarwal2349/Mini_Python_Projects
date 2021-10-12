# Insertion sort program
"""
Sample Input : A = [3, 5, 8, 9, 0, 1, 68]

Sample Output : Sorted Array in Ascending Order: [0, 1, 3, 5, 8, 9, 68]
"""
""" to get the output array in descending order, write -> while i>=0 and key > A[i] """

def Insertion_Sort(A):   # A is a given array
    
    for iter in range(1, len(A)):
        # The first element in an input array is assumed to be sorted. Take the second element and store it separately in key.
        key = A[iter]
        i = iter - 1
        
        #for Ascending order array
        # Compare key with each element on the left hand side of it until an element smaller than it is found       
        while i >= 0 and key < A[i]:  
            A[i + 1] = A[i]
            i = i - 1
        
        # Place key at after the element just smaller than it.
        A[i + 1] = key

A = [9,8,5,4,2,1]
# Original Array before Sorting
print('Original Array:',A)
# Sorted Array
Insertion_Sort(A)
print('Sorted Array in Ascending Order: ',A)

