p = int(input("How many sticks (N) in the pile? : "))
print("There are ", p," sticks in the pile.")
name = str(input("What is your name? : "))

i = 0
while (p != 0):
  n = int(input(name + ", how many stick you will take? (1 or 2): "))
  if (n > 2):
    print("No you cannot take more than 2 stick!")
  elif (n < 1):
    print("No you cannot take less than 1 stick!")
  elif (n > p):
    print("There are no enough sticks to take.")
  else:
    i += 1
    p = p-n 
    if (p == 0):
      print("OK. There is no stick left in the pile. You spent", i,"3times.")
    else:
      print("There are", p,"sticks in the pile.")