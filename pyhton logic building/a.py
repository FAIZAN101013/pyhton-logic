import random

i = 1 
while i <= 5:
    print(i)
    i = i + 1
print("Done") 
Num = random.randint(1,10)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    Num1 = int(input("Guess the Number :"))
    guess_count += 1
    if Num1 == Num :
        print("Youn won  ")
        break
    elif guess_count == 2:
        print(f"The hint is {Num - 1}")
else:  
    print(f"You lost  The number if  {Num}")

