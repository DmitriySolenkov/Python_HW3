import random
num = int(input('Введите количество элементов списка: '))
array = []
for i in range(num):
    array.append(round(random.uniform(1, 20), 3))
print(array)
rem = []
for j in range(num):
    rem.append(round(array[j] % 1, 3))
print(rem)
max = rem[0]
min = rem[0]
for k in range(num):
    if rem[k] > max:
        max = rem[k]
    if rem[k] < min:
        min = rem[k]
print(round(max-min, 3))
