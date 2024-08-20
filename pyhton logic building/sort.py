'''n = []

# Loop to take 10 inputs from the user
for _ in range(10):
    i = int(input("Enter a number: "))
    n.append(i)

# Sort the list to find the smallest number
n.sort()

print(f'The smallest number is {n[0]}')
n = []
for _ in  range(3):
    i = int(input("Enter"))
    n.append(i)
n.sort()

print(f'{n[0]}')'''

a = int(input("Enter a number: "))
c = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a<= b and a<= c:
    print(f" is the smallest {a}")
elif b<=a and b<=c:
    print(f" is the smallest {b}")
else:
    if c<=a and c<=b:
        print(f'is the smallest {c}')
    
