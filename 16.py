import random

M=random.randint(500,10000)
print("Money= " + str(M))

A=M%500
A1=M//500
print("500: " + str(A1))

B=A%100
B1=A//100
print("100:" + str(B1))

C=B%10
C1=B//10
print("10:" + str(C1))

D1=C//2
print("2:" + str(D1))
