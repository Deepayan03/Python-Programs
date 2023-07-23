print("Enter 1 to insert")
print("Enter 2 to delete")
print("Enter 3 to peek")
print("Enter 4 to print")
stack=[]
while(True):
    i=int(input("Enter your choice"))
    if(i==1):
        stack.append(int (input("Enter the number")))
    elif(i==2):
        popped=stack.pop()
        print(popped)
    elif(i==3):
        print(stack.index(int(input("Enter the number"))))
    elif(i==4):
        print(stack)
    else:
        print("Enter right input")
