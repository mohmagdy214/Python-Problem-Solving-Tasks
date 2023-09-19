
def multi_table(x,y):
    for i in range(x,y+1):
        print("---------------")
        for n in range(1,13):
            print(f'{i} X {n} = {i*n}')

multi_table(int(input('Enter Your Fnum: ')),int(input('Enter Your Fnum: ')))
