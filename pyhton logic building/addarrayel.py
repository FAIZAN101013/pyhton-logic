def sum_array(a):
    total = 0
    for i in a:
        total += i
    return total

a = []  # Initialize an empty list
#n =  5 #int(input("Enter the number of elements: "))  5 # this an be 5
for _ in range(5):
    element = int(input("Enter an element: "))
    a.append(element)

print("Sum of the array:", sum_array(a))
