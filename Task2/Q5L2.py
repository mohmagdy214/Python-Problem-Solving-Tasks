Names = ['mahmoud','farida','ali','tamer','hassan','mohamed','margot','taha']


# First Way
normal_list = []
for n in Names:
    normal_list.append(len(n))
            
            
print(normal_list)


#Second Way
normal_list2 = [len(x) for x in Names]
print(normal_list2)


#Third Way
def list3(q):
    return len(q)

normal_list3 = list(map(list3,Names))
print(normal_list3)

