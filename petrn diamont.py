row=0
while row<5:
    col=0
    while col<5:
        if row+col==2 or col-row==2 or row+col==6 or row-col==2 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    print()
    row=row+1