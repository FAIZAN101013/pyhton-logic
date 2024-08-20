# Basic Looping:Write a Python program that prints the numbers 1 to 10 using a loop.

for i in range (1,11):
    print(i)
    
    
    
for i in range (1,11):
    print(i , end=" ")  

#Write a Python program that takes a list of integers and creates a new list containing only the even numbers from the original list. Use list comprehension to solve this

a = []

for i in range(5):
    i = int(input(f"Enter the Numbers limit {5} : "))
    
    a.append(i)
print(a)

new_a = []
for i in a:
    if i%2 == 0 :
        new_a.append(i)
print(new_a)
       

# list comprihesion 
#
        
a = [int(input(f"Enter the Numbers{i+1} ; ")) for i in range(5)]
print(a)

new_a =[ i for i in a if i%2 == 0]
print(new_a)
 
def  re(s):
    return s[::-1]

list1 = [100, 200, 300, 400, 500]
list= re(list1)
print(list)

list1 = [[100, 200, 300, 400, 500] ]
print(list1[::-1])
reversed_list = list1[::-1]
print(reversed_list)
