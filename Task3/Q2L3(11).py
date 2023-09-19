
Temp_converter = {'T1':-50,'T2':-20,'T3':-2}
len_converter = {'L1':27,'L2':11,'L3':75}

'''
temp = int(input('Enter the temp: '))
len_ = int(input('Enter the len: '))
from_Fahrenheit_to_Celsius = f'{(temp-32)*5/9} C'
from_Celsius_to_Fahrenheit = f'{(temp*1.8)+32} F'
print(from_Celsius_to_Fahrenheit)

from_Inches_to_Centimeters = f'{len_*2.54} cm'
from_Centimeters_to_Inches = f'{len_*0.393700787} inch'
print(from_Centimeters_to_Inches)
'''


'''
to_Celsius = {k.replace('T','C'):(v-32)*5/9 for (k,v) in Temp_converter.items()}
to_Fahrenheit = {k.replace('T','F'):(v*1.8)+32 for (k,v) in Temp_converter.items()}
print(to_Fahrenheit)

to_Centimeters = {k.replace('L','C'):(v*2.54) for (k,v) in len_converter.items()}
to_Inches = {k.replace('L','I'):(v*0.393700787) for (k,v) in len_converter.items()}
print(to_Inches)
'''



to_Celsius = list(map(lambda v:(v-32)*5/9,Temp_converter.values()))
to_Fahrenheit = list(map(lambda v2:(v2*1.8)+32,Temp_converter.values()))

result_to_Celsius = dict(zip(Temp_converter.keys(),to_Celsius))
result_to_Fahrenheit = dict(zip(Temp_converter.keys(),to_Fahrenheit))
print(result_to_Fahrenheit)


to_Centimeters = list(map(lambda k: (k*2.54) ,len_converter.values()))
to_Inches = list(map(lambda k2:(k2*0.393700787)+32,len_converter.values()))

result_to_Centimeters = dict(zip(len_converter.keys(),to_Centimeters))
result_to_Inches = dict(zip(len_converter.keys(),to_Inches))
print(result_to_Inches)



