p = int(input("How many sticks (N) in the pile? : "))
print("There are", p, "sticks in the pile")
name = str(input("What is your name? : "))

i = 0
import random
while (p != 0):
    if (i%2 == 0):
        n = int(input(name + ", how many sticks you will take? (1 or 2) : "))
    else :
        if ((p-1)%3 == 1):
            n = 1
        elif ((p-1)%3 == 2) :
            n = 2
        else :
            n = random.randint(1,2)
        print("computer, take : ", n)
    if (n > 2):
        print("No you cannot take more than 2 sticks!\n")
    elif (n < 1):
        print("No you cannot take less than 1 stick!\n")
    elif (p-n < 0):
        print("There are no sticks enough to take.\n")
    else :
        i += 1
        p = p-n
        if (p == 0):
            if (i%2 == 0):
                print(name, ", takes the last stick.\n")
                print("Computer win !!!!")
            else :
                print("Computer, take the last stick.")
                print(name, ", Win (Computer, am sad T_T)")
        else :
            print("There are", p, "sticks in the pile.\n")
