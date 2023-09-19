Names = ['mahmoud','farida','ali','tamer','hassan','mohamed','margot','taha']
letter = 'a'

# First Way
normal_list = []
for n in Names:
        if n.count(letter)>1:
            normal_list.append(n)
            
            
print(normal_list)


#Second Way
normal_list2 = [x for x in Names if x.count(letter)>1]
print(normal_list2)


#Third Way
def list3(q):
        if q.count(letter)>1:
            return q

normal_list3 = list(filter(list3,Names))
print(normal_list3)

