import math
def checkPrime(num):
    d = 2
    while d <= math.sqrt(num):
        if num % d == 0:
            return False
        else:
            state = True
            d += 1
    return state

n = 5
total = 5               #2 + 3
while n < 2000000:
    if checkPrime(n) == True:
        total += n
    n += 2
print total

