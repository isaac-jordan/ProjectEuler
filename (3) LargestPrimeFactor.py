def GreatestPrime():
    n=input("Find largest prime factor of: ")
    start=n
    current=2
    #Finds the factors of starting number, then finds factors of factors until no longer divisble.
    while (current <= n/2):         #Prime can never be greater than half the number
        if (n % current == 0):      #Check if divisible
            n=n/current             #If divisible, divide and make n become the quotient
            current=2               #Reset current to 2
        else:
            current=current+1       #If indivisble, step current by 1
    #After this has run, n is now the largest prime factor. 
    print "Largest prime factor of ", start, " is ", n
GreatestPrime()
