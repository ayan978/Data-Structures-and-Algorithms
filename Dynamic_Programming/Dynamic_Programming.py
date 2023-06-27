#Finding nth fibonacci number

#Top-Down approach

import numpy as np
list1 = []
def fib(n):
    list1.append(0)
    list1.append(1)
    for i in range(2,n):
        list1.append(-1)
    fib_rec(n)
    print(list1[n-1])

def fib_rec(n):
    if list1[n-1] >= 0:
        return list1[n-1]
    else:
        list1[n-1] = fib_rec(n-1) + fib_rec(n-2)
        return list1[n-1]

n = int(input('Enter number of terms : '))
fib(n)

#Bottom-Up approach

def fib1(n):
    arr1[0] = 0
    arr1[1] = 1
    for i in range(2,n):
        arr1[i] = arr1[i-1] + arr1[i-2]
    return arr1[n-1]

n1 = int(input('Enter number of terms : '))
arr1 = np.empty(n,int)
print(fib1(n1))

