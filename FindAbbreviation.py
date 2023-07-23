def FindAbbreviation(s):
    list=s.split(" ")
    for i in range(0,len(list)-1):
        print(list[i][0].upper(),end='.')
    print(list[len(list)-1])




FindAbbreviation("Rajesh Kumar Sharma")
