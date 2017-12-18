__author__ = 'MaxZhuang'

A = [1, 3, 5, 6, 7, 8, 9]
x = 1

def binary_search( A, x ):
    left = 0
    right = len(A) - 1
    while( left <= right ):
        mid = (left + right) / 2
        if( A[mid] > x ):
            right = mid - 1 # x must be in lower half of list
        elif( A[mid] < x ):
            left = mid + 1 # x must be in upper half of list
        else:
            return mid # found it
    return -1 # didn't find it

print binary_search(A, x)