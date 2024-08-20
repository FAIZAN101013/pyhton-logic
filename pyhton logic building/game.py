
started = False
while True :
    s = input("> ").lower()
    if s == "help":
            print(f'''
                Start - to Start The Car
                Stop - to Stop The Carhe
                Quit - to quit the game
                ''')
          
    elif s == "start" :
                if started:
                    print("Car alredy started")
                else:
                    started = True
                    print("Car Started ... ready to go ")
    elif s == "stop":
        if not started:
            print("car aleady stoped")
        else:
            started = False
            print("car stoped")
    elif s =="quit":
                break
    else:
        print("don't understand")
                
                
            
    