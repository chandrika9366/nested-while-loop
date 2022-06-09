a=int(input("enter a"))
i=1
while i<=a:
    j=a
    while j>=i:
        print(j,end="")
        j=j-1
    print()
    i=i+1    