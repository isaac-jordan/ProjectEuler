import string

letters = " " + string.ascii_uppercase
for line in open("./data/names.txt"):
    line = line.split(",")
    line = map(lambda x: x[1:-1:], line)
    names = line

names = sorted(names)
total = 0
i = 1
for name in names:
    localTotal = 0
    for letter in name:
        localTotal += letters.index(letter)
    total += localTotal * i
    i += 1

print total
