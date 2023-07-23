def fibo(lim):
        a=0;
        b=1;
        print(a,b,"  ",end="")   
        for i in range(1,lim):
                c=a+b;
                a=b;
                b=c;
                print(b,"  ",end="")
        
fibo(int(input("Enter the limit")))
 