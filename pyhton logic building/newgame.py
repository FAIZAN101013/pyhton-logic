i1 = ""  # Initialize with an empty string
while i1 != "quit":
    s = input("> ").lower()  # Take input and convert it to lowercase
    if s == "help":
        print('''
            Start - to Start The Car
            Stop - to Stop The Car
            Quit - to quit the game
            ''')
        
    elif s == "start":
        print("Car Started ... ready to go")
        
    elif s == "stop":
        print("Car stopped.")
        
    elif s == "quit":
        print("Exiting the game...")
        break  # Exit the loop
        
    else:
        print("I don't understand that command.")
