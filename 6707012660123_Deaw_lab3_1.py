for count in range(101): #count number from 0 to 100 (range=(n-1))
    if(count == 0):
        continue #bypass 0 and start counting at 1
    if(count %2 == 0):
        print(count, "is even")
    else:
        print(count, "is odd")

