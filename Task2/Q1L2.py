Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# First Way
normal_list = []
for n in Names:
    normal_list.append(n.upper())
print(normal_list)


#Second Way
normal_list2 = [x.upper() for x in Names]
print(normal_list2)


#Third Way
def list3(nl3):
    return nl3.upper()

normal_list3 = map(list3,Names)
print(list(normal_list3))
