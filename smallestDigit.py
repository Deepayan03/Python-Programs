def findSmallest(num):
    list=[]
    while(num!=0):
        rem=num%10
        list.append(rem);
        num//=10
    min=list[len(list)-1]
    for i in range(0,len(list)):
        if(min>list[i]):
            min=list[i]
    return min

print(findSmallest(256586))
