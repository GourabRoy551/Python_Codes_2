from array import *


def findNumber(x, y):
    k = 0
    for j in x:
        if j == y:
            print('Yes')
        else:
            print('No')
            break

        k++1

arr = array('i', [])
n = int(input())

for i in range(n):
    arr.append(int(input()))

val = int(input())
result = findNumber(arr, val)




