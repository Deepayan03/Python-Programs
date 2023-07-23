list=[12,78,52,87,25]
n=len(list)
for i in range(0,n):
    min=i
    for j in range(i+1,n):
        if(list[j]<list[min]):
            min=j
    list[i],list[min]=list[min],list[i]

print(list)