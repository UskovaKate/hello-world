import array
import random

M = random.randint(1,10)
K = random.randint(1,100)
N = random.randint(1,5)

arr = [random.randint(1,10) for i in range(N)]
print("N= " + str(N))
print("K= " + str(K))
print("M= " + str(M))
print(arr)
arr2 = [ random.randint(1,100) for i in range(M)]
print(arr2)

arr.insert(K, arr2)
print(arr)
