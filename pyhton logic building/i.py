
def count_bits(n):
    b = bin(n)  # Convert the number to binary
    return b  # Return the binary string

def main():
    n = int(input("Enter the number: "))  # Get user input
    n1 = count_bits(n)  # Call the function
    print(f"Binary representation: {n1}")  # Print the binary string

main()