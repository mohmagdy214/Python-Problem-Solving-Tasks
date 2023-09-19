Names = ['mahmoud','farida','ali','tamer','hassan','mohamed','margot','taha']

# First Way
normal_list = []
for n in Names:
    if 't' in n[0]:
        normal_list.append(n)

print(normal_list)


#Second Way
normal_list2 = [x for x in Names if 't' in x[0]]
print(normal_list2)


#Third Way
def list3(q):
        if 't' in q[0]:
            return q

normal_list3 = list(filter(list3,Names))
print(normal_list3)

