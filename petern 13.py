a=int(input("enter a"))
i=1
while i<=a:
    j=1
    while j<=i:
        print(" ",end="")
        j=j+1
    l=a
    while l>=i:
        print("*",end=" ")
        l=l-1
    print()
    i=i+2    