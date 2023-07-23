def fact(n):
    a=1
    if(n==0 or n==1):
            return 1;
    for i in range(1,n+1):
        a=a*i;
    return a;

j=0
num=int(input("Enter the number"))
num1=num
while(num1!=0):
     digit=int(num1%10)
     print(digit)
     j=j+fact(digit)
     num1=num1/10;
print(j)
if(num==num1):
     print("Number is a kriushmurthy number")
else:
     print("Number is not krishnamurthy")

