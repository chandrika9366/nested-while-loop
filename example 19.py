a=int(input("enter a"))
i=1
while i<=a:
    j=1
    while j<=a:
        if i==1 or i==4 or j==1 or j==5 or i==1+j*2 or i==5-j+4:
            print("*",end=" ")
        else:
            print(" ",end=" ")  
        j=j+1    
    print()          
    i=i+1