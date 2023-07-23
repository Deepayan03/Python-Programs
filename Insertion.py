list=[78,12,6,54]
n=len(list)
for i in range(1,n):
    curr=list[i];
    j=i-1;
    while(j>=0 and list[j]>curr):
        list[j+1]=list[j]
        j=j-1;
    list[j+1]=curr;
print(list)