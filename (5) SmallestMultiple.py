#2520 is the smallest number that can be divided by each of nums from 1 to 10.
#What is smallest positive number that is evenly divisble by all nums from 1 to 20?

def main(): #Main Function 
    num = 2520
    while True:
        if checkDiv(num) == True:
            print num
            return
        else:
            num += 2520


def checkDiv(x):
    check = 0
    for y in range(1, 21):
        if x % y == 0:
            check += 1
    if check == 20:
        return True

main()
