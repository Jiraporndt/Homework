import random
z=[]
for i in range (0,4):
    z.append(input("Number: "))

x=[]
for i in range(1000):
    random.shuffle(z)
    e=int(z[0]+z[1]+z[2]+z[3])
    x.append(e)
print("Max Number is",format(max(x)))
