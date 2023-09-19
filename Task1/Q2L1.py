
def divided_by(x,y):
    result = []
    for q in range(1,101):
        if q%x == 0 and q%y == 0 :
            result.append(q)
        else:
            continue

    return result

print(divided_by(int(input('Enter Fnum: ')),int(input('Enter Snum: '))))
