def fibseq():
    first = 1
    second = 2
    added = 0
    answer = 0
    state=raw_input("even or odd numbers?")
    top=input("Max Fibonacci number?")
    while added <=top:
        added=second
        if state == "even":
            if (added % 2 == 0):
                answer=answer+added
        if state == "odd":
            if (added % 2 == 1):
                answer=answer+added
        added=first+second
        first=second
        second=added
    print answer
fibseq()
