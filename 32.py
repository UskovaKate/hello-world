import random
N=random.randint (1,100) 
arr = [random.randint (1,10) for i in range(N)]
print(arr)

for i in range(0,N,2):
    arr[i] , arr[i+1] = arr[i+1] , arr[i]

print(arr)
