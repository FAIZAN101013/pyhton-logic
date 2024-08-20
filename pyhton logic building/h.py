def fact(n):
    if n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    try:
        num_values = 5  # Number of values to calculate factorial for
        for _ in range(num_values):
            n = int(input("Enter a positive integer: "))
            if n < 0:
                print("Can't find the factorial of a negative number")
            else:
                print(f"The factorial of {n} is {fact(n)}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

main()