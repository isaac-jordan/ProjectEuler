global yMax = 2
global xMax = 2
global PathCount = 0
global path
global ListOfPaths = []

def checkDown(y):
    if y == yMax:
        return False
    return True

def checkAcross(x):
    if x == xMax:
        return False
    return True

def moveDown(y):
    y += 1
    return y

def moveAcross(x):
    x += 1
    return x

def ChooseDirection(x,y):
    global path
    if checkAcross(x) == True:
        x = moveAcross(x)
        path = path + "1"
    elif checkDown(y) == True:
        y = moveDown(y)
        path = path + "0"
    else:
        end()

def Run():
    path = ""
    x = 0
    y = 0
    if checkAcross(x) == True:
        x = moveAcross(x)
        path = path + "1"
    elif checkDown(y) == True:
        y = moveDown(y)
        path = path + "0"
    else:
        PathCount += 1
        if not any(path in s for s in ListOfPaths):
            ListOfPaths.append(path)
        else:
            
        
    
