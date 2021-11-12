n=int(input("Enter n. of rows- "))
p=n
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(p*2-1):
        print("*",end="")
    p=p-1
    print("\r")
