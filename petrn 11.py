i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end="")
        j=j+1
    b=1
    while b<=i:
        if i==b or b==1:
            print("*",end=" ") 
        elif b<=i and i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
        b=b+1
    print()
    i=i+1                  