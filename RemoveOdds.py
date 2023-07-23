def remove(num):
    number=0
    while(num!=0):
        rem=num%10
        if(rem%2==0):
            number=number*10+rem;
        num=num//10
    return number

print(remove(55025));


