squaresum = 0
sumofsquares = 0

def square():
    global squaresum
    for x in range(1, 101):
        squaresum += x**2

def sumofsquare():
    global sumofsquares
    for x in range(1, 101):
        sumofsquares += x
    sumofsquares = sumofsquares**2


square()
sumofsquare()
print sumofsquares - squaresum
    
