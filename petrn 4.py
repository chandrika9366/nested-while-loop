i=4
while i>=1:
    j=1
    while j<=4-i:
        print(" ",end="")
        j=j+1
    b=1
    while b<=i:
        if b==i or i==4:
            print("*",end=" ")  
        elif b<=i and b==1:
            print("*",end=" ")  
        else:
            print(" ",end=" ")      
        b=b+1
    print()
    i=i-1                 