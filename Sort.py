def sort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-i-1):
            if (list[j]>list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
    return list;



print(sort([1.1,8.2,2.3,1.5,5.8]))