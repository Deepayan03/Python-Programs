# 1. Write a program to find the partial abbreviation of a name. (Ex: Ram Kumar Sharma => R.K.Sharma)
# 2. Write a program to find the length of the longest word in a string. 
# 3. Write a program to count the occurrence of each word in a string. 
# 4. Write a program to removed extra spaces, if any, between the words in a string.
# -----------------------------------------------------------------------------------
# def abbriviation_name(name):
#     namelist=name.split();
#     leng=len(namelist);
#     fm=namelist[0];
#     lm=namelist[-1];
#     mms=namelist[1:-1];
#     result=fm[0]+"."
#     for m in mms:
#         result=result+m[0]+".";
#     result=result+lm;
#     print(result);
# abbriviation_name(input("Enter the name"));
# -----------------------------------------------------------------------------------
# def longest(str1):
#     list1=str1.split();
#     longeststr=0;
#     index=0;
#     for i in range(0,len(list1)-1):
#         if(longeststr < len(list1[i])):
#             longeststr=len(list1[i]);
#             index=i;
#     print("The longest word in the string is "+list1[index]);
#     print(longeststr)
# longest("The fox jumps over fucking the wall");
# -----------------------------------------------------------------------------------
# def occurances(str1):
#     words=str1.split();
#     count =0;
#     for i in range(0,len(words)):
#         for j in range(0,len(words)):
#             if(words[i]==words[j]):
#                 count+=1
#         print(words[i]+"--->"+str(count));
#         print("\n");
#         count=0;
# occurances("the fox jumps over the wall")
# -----------------------------------------------------------------------------------
# def remove_extra_spaces(s):
#     return " ".join(s.split())

# str=remove_extra_spaces("     Python  Programming")
# print(str)
# -----------------------------------------------------------------------------------


