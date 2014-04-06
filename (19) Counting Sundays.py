

def countSundays():
    sundayCount = 0
    
    year = 1900
    while year < 2001:
        if year % 4 == 0:
            days = 366
            leap = True
        else:
            days = 365
            leap = False
        day = 1
        while day < days:
            if day % 7 == 0: #This only works for the first year...
                if leap == True and day in [1,32,60,91,120,152,182,213,244,274,304,334]:
                    sundayCount += 1
                    
        
    
        
