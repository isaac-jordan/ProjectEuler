Fibs = [1,1]
i = 2
while True:
    Fibs.append(Fibs[i-2] + Fibs[i-1])
    
    if len(str(Fibs[i])) == 1000:
        print "Term: " + str(Fibs[i])
        print "Position: " + str(i+1)
        break
    i += 1
