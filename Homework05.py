import random
z=[]
a=(input("Number: "))
z.append(a)
b=(input("Number: "))
z.append(b)
c=(input("Number: "))
z.append(c)
d=(input("Number: "))
z.append(d)

x=[]
for i in range(10000):
    random.shuffle(z)
    e=int(z[0]+z[1]+z[2]+z[3])
    x.append(e)
print("Max Number is",format(max(x)))