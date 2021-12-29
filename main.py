
started = False
startGame = True

while startGame:
    keyInput = input("> ").lower()
    if keyInput == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit 
        """)
    elif keyInput == "start":
        if started:
            print("Hey!, car is already started..")
        else:
            started = True
            print("Car started.. Ready to go")
    elif keyInput == "stop":
        if not started:
            print("Hey!, car is already stopped..")
        else:
            started = False
            print("Car stopped")
    elif keyInput == "quit":
        print("game quited")
        break
    else:
        print("Sorry, I don't understand that")



