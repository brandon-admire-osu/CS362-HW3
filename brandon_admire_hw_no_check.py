while(True):
    try:
        usr_input = int(input("Please enter the year: "))
        if (usr_input < 0):
            print("Please enter a positive number, we ain't going back in time on this ride! Try again.\n")
        else:
            break
    except ValueError:
        print("That is not a number! Try again\n")
    
# usr_input = int(input("Please enter the year: "))

if (usr_input % 4 == 0):
    if (usr_input % 100 == 0 and usr_input % 400 != 0):
        print(f"{usr_input} is not a leap year.")
        exit()
    else:
        print(f"{usr_input} is a leap year!")
        exit()
else:
    print(f"{usr_input} is not a leap year.")
    exit()