def count_by(x, n):
    result = []
    for i in range( 1,n+1):
        result.append(x * i)
    return result

x = 1
n = 10
print(count_by(x, n))
