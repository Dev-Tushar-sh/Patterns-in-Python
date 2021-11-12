n=int(input("Enter number of rows- "))
for i in range(1,n):
    for j in range(n-1,i,-1):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print("\r")
