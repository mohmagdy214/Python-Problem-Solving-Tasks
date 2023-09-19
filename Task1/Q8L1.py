
def can_be_divided_by(x,y):
    for n in range(x,101):
        if n%y == 0:
            print(n)
        else:
            continue

can_be_divided_by(int(input('Enter your x: ')),int(input('Enter your y: ')))
