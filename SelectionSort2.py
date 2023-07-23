def selectionSort(list):
    n=len(list)
    min=0
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if(list[j]<list[min]):
                min=j
        list[i],list[min]=list[min],list[i]
    return list


print(selectionSort([20,10,50,25,11]))