a=int(input("enter a"))
i=1
while i<=a:
    j=1
    while j<=a-i:
        print(" ",end="")
        j=j+1
    l=1
    while l<=i:
        print("*",end=" ")
        l=l+1
    print()
    i=i+1   