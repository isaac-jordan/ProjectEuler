import time

def triplet(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False

def findAnswer():
    for b in range (0,1000):
        a = 0
        while a < b:
            if 2*a*b - 2000 *a - 2000*b + 1000000 == 0:
                c = 1000 - a - b
                print "found"
                print a,b,c
                return a*b*c
            a += 1
    return -1

t = time.clock()
print findAnswer()
print time.clock() - t
            
