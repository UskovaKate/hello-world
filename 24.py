import random

a=random.randint(1,10)
print("a= " + str(a))

b=random.randint(1,10)
print("b= " + str(b))

c=random.randint(1,10)
print("c= " + str(c))

d=random.randint(1,10)
print("d= " + str(d))

if (a <= c and b <= d) or (a <= d and b <= c):
    print("A rectangle with sides a,b can fit into a rectangle with sides c,d")

if not (a <= c and b <= d) or not (a <= d and b <= c):
    print("Rectangle with sides a,b can NOT fit into rectangle with sides c,d")
