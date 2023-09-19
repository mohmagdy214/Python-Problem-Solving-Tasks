Names = ['mahmoud','farida','ali','hassan','mohamed','john','taha']

# First Way
normal_list = []
for n in Names:
    if 'a' in n:
        normal_list.append(n)

print(normal_list)


#Second Way
normal_list2 = [x for x in Names if 'a' in x]
print(normal_list2)


#Third Way
def list3(q):
        if 'a' in q:
            return q

normal_list3 = list(filter(list3,Names))
print(normal_list3)

