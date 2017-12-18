__author__ = 'MaxZhuang'


L = [1, 2, 3, 4, 7]
total = 0

def sum_even_list(L, total = 0):
    if len(L) == 0:
        return total
    else:
        if L[0]%2 == 0:
            total = L[0] + total
            return sum_even_list(L[1:], total)
        else:
            total = total
            return sum_even_list(L[1:], total)

print sum_even_list(L,total)