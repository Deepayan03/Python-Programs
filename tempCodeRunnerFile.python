list=[1,2]
flag=0
count=0
for i in range(0,len(list)-1):
    for j in range(0,len(list)-1-i):
        if(list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
            flag=1
    count+=1
    if(flag==0):
        break

print(list)
print(count)