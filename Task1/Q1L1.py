
def get_odd_even_nums(x,y):
    even = []
    odd = []
    for n in range (x,y+1):
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return f'''the odd numbers are:{odd}

the even numbers are: {even}'''

print(get_odd_even_nums(int(input('Enter F_num: ')),int(input('Enter S_num: '))))
