import random

N = random.randint(1,100)
arr=[random.randint(-10,10) for i in range(N)]
print(arr)
K=1

for i in range(0,N):
    if arr[i] < 0:
        break
    if arr[i] >= 0:
        if arr[i] > arr[i+1] and arr[i+1] >= 0:
            K=1
            break
        if arr[i] < arr[i + 1]:
                K=2
    
if K == 1:
    print("Not increasing sequence")
elif K == 2:
    print("Increasing sequence")
