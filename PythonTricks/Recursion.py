import sys
print(sys.getrecursionlimit())

def summing(n):
    if n == 1:
        return 1
    else:
        return n + summing(n - 1)



print(summing(998))
