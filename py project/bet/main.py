import random as ran  # Import the random module for random number generation

# Constants for betting limits
MAX_LINES = 3  # Maximum number of lines to bet on
MAX_BET = 100  # Maximum amount that can be bet on a line
MIN_BET = 1    # Minimum amount that can be bet on a line

# Number of rows and columns for the slot machine
ROWS = 3
COLS = 3

# Define the count of each symbol (A, B, C, D) and their values
symbol_count = {
    "A": 2,  # Symbol 'A' appears 2 times
    "B": 4,  # Symbol 'B' appears 4 times
    "C": 6,  # Symbol 'C' appears 6 times
    "D": 8   # Symbol 'D' appears 8 times
}
symbol_value = {
    "A": 5,  # Value for symbol 'A'
    "B": 4,  # Value for symbol 'B'
    "C": 3,  # Value for symbol 'C'
    "D": 2   # Value for symbol 'D'
}

def check_win(columns, lines, bet, symbol_value):
    """
    Checks if there are winning lines and calculates winnings.
    
    Args:
        columns (list): The slot machine result.
        lines (int): Number of lines bet on.
        bet (int): Bet amount per line.
        symbol_value (dict): Dictionary of symbol values.
    
    Returns:
        tuple: Total winnings and list of winning lines.
    """
    wins = 0  # Initialize total winnings
    winline = []  # List to store winning lines
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol in the first column for the current line
        for column in columns:
            symbol_to_check = column[line]  # Get the symbol for the current line in each column
            if symbol != symbol_to_check:  # Check if all symbols match
                break
        else:
            # If all symbols match, calculate winnings
            wins += symbol_value[symbol] * bet
            winline.append(line + 1)  # Add the line number to the list of winning lines
    return wins, winline

def get_m_spin(rows, cols, symbol_count):
    """
    Generates a random spin result for the slot machine.
    
    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbol_count (dict): Dictionary containing symbol counts.
    
    Returns:
        list: A list of lists representing the spin result (each sublist corresponds to a column).
    """
    all_sym = []  # List to store all symbols according to their counts
    for symbol, count in symbol_count.items():
        all_sym.extend([symbol] * count)  # Add each symbol to the list according to its count

    columns = []  # List to store the result for each column
    for _ in range(cols):
        current_symbols = all_sym[:]  # Copy the list of all symbols for each column
        column_result = []  # List to store the result for the current column
        for _ in range(rows):
            value = ran.choice(current_symbols)  # Randomly select a symbol
            current_symbols.remove(value)  # Remove the selected symbol from the list
            column_result.append(value)  # Add the symbol to the column result
        columns.append(column_result)  # Add the column result to the final columns list
    return columns

def print_machine(columns):
    """
    Prints the slot machine's spin result in a formatted way.
    
    Args:
        columns (list): List of lists representing the spin result (each sublist corresponds to a column).
    """
    for row in range(len(columns[0])):  # Loop through each row
        for i, column in enumerate(columns):  # Loop through each column
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print symbol with separator
            else:
                print(column[row], end="  ")  # Print symbol without separator (last column)
        print()  # Move to the next line after printing all columns for the current row

def deposit():
    """
    Prompts the user to input a deposit amount.
    
    Returns:
        int: The deposited amount.
    """
    while True:
        amount = input("Deposit amount: $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break  # Exit loop if amount is valid
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number.")
    return amount

def num_of_line():
    """
    Prompts the user to input the number of lines to bet on.
    
    Returns:
        int: The number of lines.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break  # Exit loop if lines are within the valid range
            else:
                print(f"Enter a valid number of lines between 1 and {MAX_LINES}.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    """
    Prompts the user to input the betting amount.
    
    Returns:
        int: The betting amount.
    """
    while True:
        bet = input(f"Enter the amount ({MIN_BET} - {MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break  # Exit loop if bet is within the valid range
            else:
                print(f"Bet amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet

def spin(balance):
    """
    Manages a single spin of the slot machine.
    
    Args:
        balance (int): The current balance.
    
    Returns:
        int: The net result of the spin (winnings - total bet).
    """
    lines = num_of_line()  # Get the number of lines to bet on

    while True:
        bet = get_bet()  # Get the betting amount
        total_bet = bet * lines  # Calculate the total bet amount

        if total_bet > balance:
            print(f"Insufficient balance. Your balance is: ${balance}")
        else:
            break  # Exit loop if total bet is within the balance

    print(f"Deposited amount: ${balance}")
    print(f"Number of lines bet on: {lines}")
    print(f"You're betting ${total_bet} on {lines} lines, and your remaining balance is ${balance - total_bet}")

    slot = get_m_spin(ROWS, COLS, symbol_count)  # Generate the spin result
    print_machine(slot)  # Print the result

    winnings, winline = check_win(slot, lines, bet, symbol_value)  # Check for winnings
    print(f"Your winnings are ${winnings}")
    print(f"You won on lines: {', '.join(map(str, winline))}")
    balance += winnings  # Update balance with winnings
    print(f"After winning, your balance is ${balance}")
    return winnings - total_bet  # Return the net result of the spin

def main():
    """
    Main function that controls the flow of the slot machine game.
    """
    balance = deposit()  # Get the initial deposit
    while True:
        print(f"Current balance is ${balance}")
        spin1 = input("Press enter to spin (q to quit): ")
        if spin1.lower() == "q":
            break  # Exit loop if user inputs 'q'
        balance += spin(balance)  # Perform a spin and update balance
    print(f"You are left with ${balance}")  # Print the final balance

# Run the main function to start the game
main()