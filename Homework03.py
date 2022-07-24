p = int(input("How many sticks (N) in the pile? : "))
print("There are", p, "sticks in the pile")
name = str(input("What is your name? : "))

i = 0
import random
while (p != 0):
    if (i%2 == 0):
        n = int(input(name + ", how many sticks you will take : "))
        if (n > 2):
            print("No you cannot take more than 2 sticks!\n")
        elif (n < 1):
            print("No you cannot take less than 1 stick!\n")
        elif (n > p):
            print("There are no sticks enough to take.\n")
        else :
            i += 1
            p = p-n
            if (p == 0):
                print(name, ", takes the last stick.")
                print("Computer win !!!!")
            else :
                print("There are", p, "sticks in the pile.\n")
    else :
        com = random.randint(1,2)
        print("computer, take : ", com)
        if (p - com < 0):
            print("There are no enough sticks to take.")
        else :
            p = p-com
            i += 1
            if (p == 0):
                print("Computer, take the last stick.")
                print(name, ", Win (Computer, am sad T_T)")
            else :
                print("There are", p, "sticks in the pile.\n")