from math import factorial
def fact(n):
    if n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1): # whta happns where result =1 , the first ittration  result bemon 1,2,6,24,120
            result *= i
        return result

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
                print("Can't find the factorial of a negative number")
        else:
                print(f"The factorial of {n} is {fact(n)}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

main()


for i  in range(0,5):
    i *= i


def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1) # htis what happing 5(4(3(2(1))))

num = int(input("Enter a positive integer: "))
if num < 0:
    print("Can't find the factorial of a negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {fact(num)}")
    
    
    
    

