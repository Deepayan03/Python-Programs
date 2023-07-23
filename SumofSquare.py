def SumofSquare(n):
    digits=str(n);
    sum=0;
    for digit in digits:
        sum=sum+(int(digit)**2);
    return sum;

print(SumofSquare(input()));
