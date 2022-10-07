import random
num = int(input('Введите количество элементов списка: '))
array = []
for i in range(num):
    array.append(random.randint(1, 10))
print(array)
mult = []
length = int(num/2)
if num % 2 == 0:
    for j in range(length):
        mult.append(array[j]*array[-j-1])
else:
    for j in range(length+1):
        mult.append(array[j]*array[-j-1])
print(mult)
