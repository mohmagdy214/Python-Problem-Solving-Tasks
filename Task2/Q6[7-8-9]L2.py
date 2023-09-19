Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

a1,*b1 = Names  # a= the first index , b = rest of the list
a2,*r2,b2 = Names # a = the first index , b = the last index
a3,b3,*r3 = Names # a = the first index , b = the second index

print(a3,b3)
