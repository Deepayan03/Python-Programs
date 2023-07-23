# 21.	Define a class Employee to store the information ( id, name and Basic salary) of an employee. Write a program to print the information of all employee in descending order of basic salary.
class Employee:
    def __init__(self,id,name,basic_sal):
        self.id=id
        self.name=name
        self.basic_sal=basic_sal

    def display(self):
        print(self.id)
        print(self.name)
        print(self.basic_sal)


list=[]

limit=int(input("Enter the number of employees you want to enter details of"))

for i in range(0,limit):
    name=input("Enter the name")
    id=int(input("Enter id"))
    basic_sal=int(input("Enter Basic sal"))
    a=Employee( id,name,basic_sal)
    list.append(a);
    list[i].display();

print(" ");


for i in range(0,len(list)):
    for j in range(0,len(list)-i-1):
        if(list[j].basic_sal<list[j+1].basic_sal):
            list[j],list[j+1]=list[j+1],list[j]

for i in range(len(list)):
    list[i].display();

