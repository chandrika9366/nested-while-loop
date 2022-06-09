a=int(input("enter number"))
row=1
while row<=a:
    col=1
    while col<=row:
        print("*",end="")
        col=col+1
    print()
    row=row+1