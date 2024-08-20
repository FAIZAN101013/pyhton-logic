def maps(a):
    a1 = [] 
    for element in a:
        modified_element = element *2
        a1.append(modified_element)
    return a1
##SIMILAR METHOD##
def maps(a):
    return [2 * x for x in a]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
result = maps(a)
print(result)
