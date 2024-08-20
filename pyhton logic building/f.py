'''num = [5,2,5,2,2]
for i in num:
    print('x'* i)
    '''
num = [5,2,5,2,2]
for i in num:
    result = ''
    for _ in range(i):
        result += 'x'
    print(result) 

