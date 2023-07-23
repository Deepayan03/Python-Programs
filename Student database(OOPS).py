class student:
    def __init__(self,name,roll,marks):
        self.name=name;
        self.roll=roll
        self.marks=marks

    def display(self):
        print("Name  Roll  Marks")
        print(self.name ,"   ", self.roll,"   ",self.marks," ")


studentlist=[]
limit=int(input("Enter the limit"));
for i in range(limit):
    name=input("Enter the name")
    roll=int(input("Enter the roll"))
    marks=int(input("Enter the marks"))
    sb= student(name,roll,marks)
    studentlist.append(sb);

#display part

for list in studentlist:
    list.display();

studentlist.sort(key=lambda a: a.marks, reverse=True)
for list in studentlist:
    list.display();
