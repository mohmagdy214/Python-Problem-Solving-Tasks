
from datetime import datetime

date1 =  datetime.strptime(input('Enter F_date: '), "%d-%B-%Y")
date2 =  datetime.strptime(input('Enter S_date: '), "%d-%B-%Y")
#input must be like this "02-July-2023"
result = date2 - date1

print(result)



              
