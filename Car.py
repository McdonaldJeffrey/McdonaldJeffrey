command =""
started = False
while True:
    command = input(">").lower()
    if command =="start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print(" The car is started!")
    elif command =="stop":
        if not started:
            print(" Car is stopped already!")
        else:
            started = False
            print("The car is stopped!")
    elif command == "help":
        print("""
start: Start the car
stop: Stop the car
quit: To quit the game""")
    elif command =="quit":
        break
else:
    print("I dont understand the code")


