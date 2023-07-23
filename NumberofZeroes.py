# 19.	Write a function to count the total number of Zeros in a number. Use this function in a program

def countZeroes(num):
    count=0
    while(num!=0):
        if(num%10==0):
            count=count+1;
        num//=10;
    return count;


print(countZeroes(1000000000))