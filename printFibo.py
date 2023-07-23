def printFibo(n):
    a=0
    b=1
    print(str(a)+" ",end="")
    print(str(b)+" ",end="")
    for i in range(1,n):
        c=a+b
        a=b
        b=c
        print(str(c)+" ",end="")
printFibo(5)