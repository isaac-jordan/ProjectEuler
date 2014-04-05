import math
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##
##What is the 10 001st prime number?



def checkPrime(num):
    d = 2
    while d <= math.sqrt(num):
        if num % d == 0:
            return False
        else:
            state = True
            d += 1
    return state

def getNthPrime(n):
    PrimeNum = 2
    num = 3
    while PrimeNum < n:
        num += 2
        if checkPrime(num) == True:
            PrimeNum += 1
            print "The prime with index",PrimeNum,"is",num

    
