def multiples(multiple1, multiple2, rangelower, rangehigher):
    sumx=0
    for x in range(rangelower, rangehigher):
        if (x % multiple1 == 0) or (x % multiple2 == 0):
                    sumx=sumx+x
    print sumx
multiple1=input("Enter first multiple: ")
multiple2=input("Enter second multiple: ")
rangelower=input("Enter lower range: ")
rangehigher=input("Enter higher range: ")
multiples(multiple1, multiple2, rangelower, rangehigher)

    
        
    
    
