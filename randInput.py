import random
num = int(input("give the number of random numbers to sort: "))
arr = []
for i in range(num):
        arr.append(random.randint(0,10000))
print(arr)
