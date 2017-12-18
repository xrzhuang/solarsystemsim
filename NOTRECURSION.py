__author__ = 'MaxZhuang'
A = [1, 4, 5, 7, 8, 9]
x = 1

def search(A,x):
    left = 0
    right = len(A) - 1
    while (left <= right):
        midpoint = (right + left)/2
        if A[midpoint] == x:
            return midpoint
        elif x > A[midpoint]:
            left = midpoint + 1
        else:
            right = midpoint -1
    return -1

print search(A, x)