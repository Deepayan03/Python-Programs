def InsertionSort(list):
    n=len(list)
    for i in range(0,n):
        temp=list[i]
        j=i-1
        while(j>=0 and temp<list[j]):
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp;
    return list


print(InsertionSort([20,10,50,15,12]))

