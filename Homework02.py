p = int(input("How many sticks (N) in the pile? : "))
print("There are " , p, " sticks in the pile.")
name = str(input("What is your name? : "))

i = 0
while p != 0:
  n = int(input(name + " How many sticks will you take :"))
  if n > 2:
    print("No you cannot take more than 2 sticks!")
  elif n < 1:
    print("No you cannot take less than 1 sticks!")
  elif n > p:
    print("There are no enough sticks to take.")
  else :
    i += 1
    p = p-n
    if p == 0:
      print("OK. There is no sticks left in the pile. You spent", i, "times.")
    else :
      print("There are" , p, "sticks in the pile")