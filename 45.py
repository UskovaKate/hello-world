import random

N = random.randint(1,100)
arr = [random.randint(-10,10) for i in range(N)]
print(arr)
sum_plus = 0
sum_minus = 0

for i in range(N):
    if arr[i] > 0:
        sum_plus += arr[i]
    elif arr[i] < 0:
        sum_minus += arr[i]

print("Sum plus number= " + str(sum_plus)) 
print("Sum minus number= " + str(-sum_minus)) 

if sum_plus > -sum_minus:
    arr.append(-(sum_minus + sum_plus))
elif sum_plus < -sum_minus:
    arr.append(-(sum_plus + sum_minus))

print(arr)
