from math import *

def numOfDivisors(n):
    m = 2
    i = 1
    root = sqrt(n)
    while i <= root:
        if n % i == 0:
            m += 2
        i += 1
    print m
    return m

def TriangleNums():
    i = 1
    n = 0
    while True:
        n += i
        if numOfDivisors(n) > 500:
            return n
        i += 1

print TriangleNums()


