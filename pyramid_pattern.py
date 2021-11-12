
for i in range(1,11):
    for j in range(10,i,-1):
        print(" ",end="")
    for k in range(i*2-1):
        print("*",end="")
    print("\r")
