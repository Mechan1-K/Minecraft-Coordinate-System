import time

def display(x):
    for i in range(len(x)):
        print(f"{i} | {x[i][0]} {x[i][1]} {x[i][2]} {'.' * (18 - len(str(x[i][0]) + str(x[i][1]) + str(x[i][2])))} | {x[i][3]}")

def save():
    save_file = open(r"_internal\save.txt", "w")
    save_file.write(str(system))
    save_file.close()

save_file = open(r"_internal\save.txt", "r")
system = eval(save_file.read())
print(system)
save_file.close()

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
            x | save data and exit
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
            print("Saving data...")
            try:
                save()
                print("Data written, goodbye!")
                running = False
            except:
                print("Something went wrong...")
        case _:
            print("Command unrecognized, please try again.")

save()