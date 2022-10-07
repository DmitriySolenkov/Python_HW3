import random
num = int(input('Введите количество элементов списка: '))
array= []
for i in range(num):
    array.append(random.randint(1,10))
print (array)
sum=0
for j in range(num):
    if j%2!=0:
        sum+=array[j]
print (sum)
