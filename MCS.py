import time
system = [[0, 0, 0, "This is an example"]]

def display(x):
    for i in range(len(x)):
        print(f"{i} | {x[i][0]} {x[i][1]} {x[i][2]} {'.' * (18 - len(str(x[i][0]) + str(x[i][1]) + str(x[i][2])))} | {x[i][3]}")

LINE = "-------------------------"
running = True

while running:
    print("")
    print(LINE)
    display(system)
    print("")
    print("Please enter a command (try \"help\"):")
    command = input(">")
    match command:
        case "help":
            print("""
            Here's a list of the commands:
            + | start adding an item to the system
            - | remove an item from the system
            x | exit and stop running the program
            """)
            time.sleep(5)
        case "+":
            appendee = []
            appendee.append(int(input("X position:")))
            appendee.append(int(input("Y position:")))
            appendee.append(int(input("z position:")))
            appendee.append(input("description:\n"))
            system.append(appendee)
        case "-":
           deletionee = int(input("What index position? [int]\n"))
           del system[deletionee]
        case "x":
            print("Goodbye!")
            running = False
        case _:
            print("Command unrecognized, please try again.")