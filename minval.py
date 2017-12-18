__author__ = 'MaxZhuang'
def min_val(L, current = None):
    if len(L) == 0:
        return current
    else:
        if current == None:
            current = L[0]
        if current > L[0]:
            current = L[0]
            return min_val(L[1:], current)
        else:
            return min_val(L[1:], current)

L = [9, 3, 5, 6, 7, 8]


print min_val(L)