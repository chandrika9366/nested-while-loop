a=int(input("enter a"))
i=1
while i<=a:
    j=1
    while j<=a:
        if i==1 or i==3 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")  
        j=j+1
    print()
    i=i+1          