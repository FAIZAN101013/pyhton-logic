IN = str(input("Enter a string: "))

v = 0
c = 0
for i in IN:
    if i in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
        v +=1
    elif i.isalpha():
        c +=1
print(f' Vowels : {v} and the Constants: {c}')
for i in IN:
    if i in ('a', 'A'):
        v +=1
    elif  i.isalpha() :
        c +=1
print(f' Vowels : {v} and the Constants: {c}')

IN = input("Enter a string: ").lower()

vowels = sum(1 for i in IN if i in 'aeiou')
consonants = sum(1 for i in IN if i.isalpha() and i not in 'aeiou') # this is string comprihesion

print(f'Vowels: {vowels} and Consonants: {consonants}')

        