def fact(n):
    if (n==0 or n==1):
        return 1;
    else:
        return n*fact(n-1)
    

def isPeterson(nums):
    sum=0
    for num in nums:
        sum=sum+fact(int(num))
    if(int(nums)==sum):
        return True;
    else:
        return False;
    


print(isPeterson(input()))
