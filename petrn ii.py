a=int(input("enter a"))
r=1
while r<=a:
    j=1
    while j<=a-r:
        print(" ",end="")
        j=j+1
    c=r
    while c>=1:
        print(c,end="")
        c=c-1
    c=c+2
    while c<=r:
        print(c,end="") 
        c=c+1
    print()
    r=r+1       