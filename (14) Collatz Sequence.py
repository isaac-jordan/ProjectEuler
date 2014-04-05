def parityEven(n):
    if n % 2 == 0:
        return True
    return False

def collatz(n):
    chainlength = 1
    while n != 1:
        if parityEven(n) == True:
            n = n/2
            chainlength += 1
        else:
            n = 3*n + 1
            chainlength += 1
    return chainlength
    
start = 1
maxchain = 0
while start < 1000000:
    currchain = collatz(start)
    if currchain > maxchain:
        maxchain = currchain
        maxstart = start
    start += 1
print maxchain
print maxstart
    
