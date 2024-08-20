def invert(lst):
    lst1  = []
    for i in lst:
        if i < 0:
            lst1.append(-i)
        elif i > 0:
            lst1.append(-i)
        else:
            lst1.append(i)
    return lst1
    
            
lst = [1, 2, 3, 4, 5]
print(invert(lst))