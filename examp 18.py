a=int(input("enter a"))
i=1
while i<=a:
    j=1
    while j<=a:
        if i==1 or i==5 or j==1 or j==1+i*2 or j==5-i+4:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
        j=j+1    
    print()
    i=i+1          