__author__ = 'MaxZhuang'
def reverse(S, string = ""):
    if len(S) == 0:
        return string
    else:
        temp = S[0]
        S[0] = S[len-1]
        string.append.S[0]
        S[len-1] = temp
        string.append.S[len-1]
        return reverse(S[1: len- 2])

reverse("ME")