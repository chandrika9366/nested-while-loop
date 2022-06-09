a=int(input("enter a"))
i=1
while i<=a:
    l=1
    while l<=a-i:
        print(" ",end="")
        l=l+1
    k=1
    while k<=i:
        print(i,end="") 
        k=k+1
    print()
    i=i+1       