def findfactors(num):
   
   factors=[]
   while(num%2==0):
      factors.append(2)
      num//=2;
   i=3
   while(i<num/2):
      if(num%i==0):
         factors.append(i)
         num//=i
      else:
         i+=2
   if(num>2):
      factors.append(num)
   return factors

   


print(findfactors(84));
