a=int(input("enter a"))
i=1
while i<=a:
    j=1
    while j<=a-i:
        print(" ",end="")
        j=j+1
    b=1
    while b<=i:
        if i==b or b==1 or i==a:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        b=b+1
    print()
    i=i+1                