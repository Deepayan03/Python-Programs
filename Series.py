# 18.	Write a program to print the series as given along with the sum:
# 10 – 20 + 30 – 40 + 50 - …. Upto n terms.



series=[]
n=int(input("Enter the limit"))
sum=0
term=10
for i in range(1,n):
    term=10*i
    if(i%2==0):
        term*=-1;
    series.append(str(term))
    sum+=term;
print("+".join(series));
print(sum);