def reverse(x):
    y= str(x)
    z= y[::-1]
    x=int(z)
    return x

def main():
    num1 = 100
    largest=0
    while (num1<1000):
        for num2 in range(100, 1000):
            product = num1*num2
            if product == reverse(product):
                print product
                if product>largest:
                    largest=product
        num1=num1+1
    print "The largest value is ", largest

main()
print "End"
    
            
        
