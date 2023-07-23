# 3.	Write a program to print for n number of lines
#            1
#           010
#          10101
#         0101010


def printPattern(n):
   for i in range(1, n+1):
    # Print spaces
    for j in range(1, n-i+1):
        print(" ", end="")
    
    # Print 0's and 1's
    for k in range(1, 2*i):
        if k % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    
    print() 


printPattern(5)