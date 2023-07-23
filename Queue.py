print("Enter 1 to insert")
print("Enter 2 to delete")
print("Enter 3 to peek")
print("Enter 4 to print")
queue=[]
while(True):
    i=int(input("Enter your choice"))
    if(i==1):
        queue.insert(0,int (input("Enter the number")))
    elif(i==2):
        popped=queue.pop(0)
        print(popped)
    elif(i==3):
        print(queue.index(int(input("Enter the number"))))
    elif(i==4):
        print(queue)
    else:
        print("Enter right input")
