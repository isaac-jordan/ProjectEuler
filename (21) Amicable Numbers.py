# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import time

def divisorSum(n):
    i = 1
    total = 0
    while i < (n/2)+1:
        if n % i == 0:
            total += i
        i += 1
    return total

def buildDivisorDict():
    divDict = {}
    i = 0
    while i < 10000:
        divDict[i] = divisorSum(i)
        i += 1
    return divDict

def checkAmicable(a, divDict):
    b = divDict[a]
    if b not in divDict.keys():
        divDict[b] = divisorSum(b)
    if divDict[b] == a and a != b:
        return True
    return False

def main():
    start = time.clock()
    divDict = buildDivisorDict()
    total = 0
    for i in range(1, 10000):
        if checkAmicable(i, divDict):
            print str(i) + " is amicable!"
            total += i
    print "Sum of these: " + str(total)
    end = time.clock()
    print end - start

main()
