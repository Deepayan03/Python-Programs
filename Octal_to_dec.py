def octaltodec(dec):
    if(dec<=0):
        return 0;
    octaldig=0
    a=[]
    while(dec>0):
        octaldig=dec%8;
        a.append(str(octaldig))
        dec//=8
    a.reverse()
    return "".join(a)


a=int(input("Enter the decimal number"))
print(octaltodec(a));