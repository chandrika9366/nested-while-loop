a=int(input("enter a"))
i=1
while i<=a:
    b=1
    while b<=a-i:
        print(" ",end="")
        b=b+1
    k=1
    while k<=i:
        if k==1 or i==a or k==i:
            print("*",end="") 
        else:
            print(" ",end="")    
        k=k+1
    print()
    i=i+1               