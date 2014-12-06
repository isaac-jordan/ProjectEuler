def numsToWords(n):
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['','','twenty','thirty','forty','fifty','sixty','seventy', 'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion']

    nString = str(n)
    i = 0
    words = []
    digits = []
    for digit in nString[::]:
        digits.append(int(digit))

    while i < len(nString):
        if i == len(digits)-1:
            if digits[i] != 0 and digits[i-1] == 0:
                words.append('and')
            words.append(units[digits[i]])
        elif i == len(digits)-2:
            if len(digits)>2 and digits[i] != 0:
                words.append('and')
            if digits[i] == 1:
                words.append(teens[digits[i+1]])
                break
            else:
                words.append(tens[digits[i]])
        elif i == len(digits)-3 and digits[i] != 0:
            words.append(units[digits[i]])
            words.append('hundred')
        elif i == len(digits)-4:
            words.append(units[digits[i]])
            words.append(thousands[digits[i]])
        i += 1
    return words

allNums = ""
for i in range(1,1001):
    for word in numsToWords(i):
        allNums += word

print "Number of characters: " + str(len(allNums))
